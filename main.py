from flask import Flask, request, render_template, send_from_directory

from app.core.qa_data import clean_report, clean_report_av, clean_report_granular
from app.core.json_update import process_json_input, update_json_av
from app.core.battery_life import battery_life
from app.core.matrix import matrix_file

from app.config.paths import JSON_PATH_AV
import app.config.config as config
import json
import os

# Create a Flask app
app = Flask(__name__)
app.use_static_for = 'static'

# Loading config
app.config.from_object(config)

# Validate password
def is_valid_password(password):
    return password == app.config['VALID_PASSWORD']

# Validate extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['VALID_FILE_EXTENSIONS']

# Route for file upload
@app.route('/app1', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        password = request.form.get('password')
        if is_valid_password(password):
            return render_template('index2.html')  # Render index2 template if password is valid
        else:
            return render_template('error.html', error_message='Incorrect password')  # Render error template if password is invalid
    return render_template('index.html')  # Render index page

# Route for regular files
@app.route('/scs-upload-file', methods=['POST'])
def process_file():
    if 'ph_regular' in request.files:
        file = request.files['ph_regular']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                clean_report(file)  # Process the file
                return send_from_directory('.', filename='scs_qa.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors

    elif 'av_regular' in request.files:
        file = request.files['av_regular']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                clean_report_av(file)  # Process the AV report file
                return send_from_directory('.', filename='scs_qa.xlsx', as_attachment=True)  # Serve AV report file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors

    return render_template('error.html', error_message='No file part in request'), 400  # Render error template for bad requests

# Route for processing granular files
@app.route('/scs-granular-file', methods=['POST'])
def process_file_granular():
    if 'granular' in request.files:
        file = request.files['granular']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                clean_report_granular(file)  # Process the granular file
                return send_from_directory(directory='.', filename='scs_granular_qa.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors
    return render_template('error.html', error_message='No file part in request'), 400  # Render error template for bad requests

# Route for battery life
@app.route('/scs-battery-life', methods=['POST'])
def process_file_battery():
    if 'battery' in request.files and 'life' in request.files:
        file = request.files['battery']
        file2 = request.files['life']
        try:
            if allowed_file(file.filename) and allowed_file(file2.filename):  # Check if both files have a valid extension
                battery_life(file, file2)  # Process the battery life
                return send_from_directory(directory='.', path='Battery_Life_QA.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors
    return render_template('error.html', error_message='No file part in request'), 400  # Render error template for bad requests

# Route for matrix file
@app.route('/scs-matrix-file', methods=['POST'])
def process_file_matrix():
    if 'matrix' in request.files:
        file = request.files['matrix']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                matrix_file(file)  # Process the matrix file
                return send_from_directory(directory='.', path='matrix.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors
    return render_template('error.html', error_message='No file part in request'), 400  # Render error template for bad requests

# Route for uploading JSON files
@app.route('/scs-json-upload', methods=['POST'])
def json_update():
    # Get the form inputs for both sets of variables
    tag = request.form.get('tag')
    component = request.form.get('component')
    value = request.form.get('value')
    
    tag_av = request.form.get('tag_av')
    component_av = request.form.get('component_av')
    value_av = request.form.get('value_av')
    
    # Check for the first set of variables (tag, component, value)
    if tag and component and value:
        try:
            # Call the process_json_input function with the user inputs
            process_json_input(tag, component, value)
            return render_template('file_uploaded.html')  # Render success template if processing is successful
        except FileNotFoundError as e:
            # Handle the specific case where the JSON file is not found
            return render_template('error.html', error_message=str(e)), 404  # Return a 404 Not Found status code
        except Exception as e:
            # Handle other exceptions
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors
    
    # Check for the second set of variables (tag_av, component_av, value_av)
    elif tag_av and component_av and value_av:
        try:
            # Call the update_json_av function with the alternative variables
            update_json_av(tag_av, component_av, value_av)
            return render_template('file_uploaded.html')  # Render success template if processing is successful
        except FileNotFoundError as e:
            # Handle the specific case where the JSON file is not found
            return render_template('error.html', error_message=str(e)), 404  # Return a 404 Not Found status code
        except Exception as e:
            # Handle other exceptions
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors

    # If neither set of variables is fully provided, render an error
    return render_template('error.html', error_message='Missing required fields'), 400  # Render error template for missing fields
# Route for reviewing JSON files
@app.route('/scs-json-review', methods=['GET'])
def json_review():
    filename = request.args.get('filename')
    if filename:
        try:
            file_path = os.path.join(JSON_PATH_AV, filename + '.json')
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    return render_template('json_review.html', json_data=json.dumps(data, indent=4))  # Render template to display JSON data
            else:
                return render_template('error.html', error_message='File not found'), 400  # Render error template for file not found
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=str(e)), 500  # Render error template for server errors
    return render_template('json_review.html', json_data=None)  # Render template with no JSON data

# Routes for pages
@app.route('/scs-mainpage')
def mainpage():
    return render_template('index2.html')

@app.route('/scs-user_guide')
def user_guide():
    return render_template('user_guide.html')

@app.route('/scs-regular-content')
def regular_content():
    return render_template('regular_content.html')

@app.route('/scs-granular-content')
def granular_content():
    return render_template('granular_content.html')

@app.route('/scs-battery-life')
def battery_life_content():
    return render_template('battery_life.html')

@app.route('/scs-matrix-file')
def matrix_file_content():
    return render_template('matrix_file.html')

@app.route('/scs-json-upload')
def upload_json():
    return render_template('json_update.html')

if __name__ == '__main__':
    app.run(debug=True)
