from flask import Flask, request, render_template, send_from_directory

from app.core.qa_granular import clean_granular
from app.core.battery_life import battery_life
from app.core.qa_data import clean_report
from app.core.matrix import matrix_file
from app.config.paths import JSON_PATH

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
    if 'Regular' in request.files:
        file = request.files['Regular']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                clean_report(file)  # Process the file
                return send_from_directory('.', filename='SCS_QA.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
    return render_template('error.html', error_message=e), 400  # Render error template for bad requests

# Route for processing granular files
@app.route('/scs-granular-file', methods=['POST'])
def process_file_granular():
    if 'Granular' in request.files:
        file = request.files['Granular']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                clean_granular(file)  # Process the granular file
                return send_from_directory('.', filename='Granular_QA.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
    return render_template('error.html', error_message=e), 400  # Render error template for bad requests

# Route for battery life
@app.route('/scs-battery-life', methods=['POST'])
def process_file_battery():
    if 'battery' in request.files:
        file = request.files['battery']
        file2 = request.files['life']
        
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                battery_life(file,file2)  # Process the battery life
                return send_from_directory('.', filename='Battery_Life_QA.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
    return render_template('error.html', error_message=e), 400  # Render error template for bad requests


# Route for matrix file
@app.route('/scs-matrix-file', methods=['POST'])
def process_file_matrix():
    if 'matrix' in request.files:
        file = request.files['matrix']
        
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                matrix_file(file)  # Process the matrix life
                return send_from_directory('.', filename='matrix.xlsx', as_attachment=True)  # Serve file for download
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
    return render_template('error.html', error_message=e), 400  # Render error template for bad requests


# Route for uploading JSON files
@app.route('/scs-json-upload', methods=['POST'])
def json_upload():
    if 'uploadjson' in request.files:
        file = request.files['uploadjson']
        try:
            if allowed_file(file.filename):  # Check if the file has a valid extension
                filename = file.filename
                file_path = os.path.join(JSON_PATH, filename)
                file.save(file_path)
                return render_template('file_uploaded.html')  # Render success template if file is uploaded successfully
        except Exception as e:
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
    return render_template('error.html', error_message=e), 400  # Render error template for bad requests

# Route for reviewing JSON files
@app.route('/scs-json-review', methods=['GET'])
def json_review():
    filename = request.args.get('filename')
    if filename:
        try:
            file_path = os.path.join(JSON_PATH, filename + '.json')
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    return render_template('json_review.html', json_data=json.dumps(data, indent=4))  # Render template to display JSON data
            else:
                return render_template('error.html', error_message=e), 400  # Render error template for file not found
        except Exception as e: 
            print(e)
            return render_template('error.html', error_message=e), 500  # Render error template for server errors
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
    return render_template('json_upload.html')

if __name__ == '__main__':
    app.run(debug=True) 
