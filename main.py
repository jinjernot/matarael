from flask import Flask, request, render_template, send_from_directory
from data.qa_data import clean_report

import config
import json
import os

app = Flask(__name__)
app.use_static_for = 'static'

# Configuration
app.config.from_object(config)

def is_valid_password(password):
    return password == app.config['VALID_PASSWORD']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['VALID_FILE_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        password = request.form.get('password')
        if is_valid_password(password):
            return render_template('index2.html')
        else:
            return render_template('error_password.html')
    return render_template('index.html')

@app.route('/upload-file', methods=['POST'])
def process_file():
    if 'Regular' in request.files:
        file = request.files['Regular']
        try:
            if allowed_file(file.filename):
                clean_report(file)
                return send_from_directory('.', filename='SCS_QA.xlsx', as_attachment=True)
        except Exception as e:
            print(e)
            return render_template('error.html'), 500

    elif 'JSON' in request.files:
        file = request.files['JSON']
        try:
            if allowed_file(file.filename):
                filename = file.filename
                file.save(app.config['UPLOAD_DIRECTORY'] + filename)
                return render_template('file_uploaded.html')
        except Exception as e:
            print(e)
            return render_template('error.html'), 500

    return render_template('error.html'), 400

@app.route('/json-review', methods=['GET'])
def json_review():
    filename = request.args.get('filename')
    if filename:
        try:
            file_path = os.path.join('/home/garciagi/SCS_Tool/json', filename + '.json')
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    return render_template('json_review.html', json_data=json.dumps(data, indent=4))
            else:
                return "File not found"
        except Exception as e:
            print(e)
            return render_template('error_json.html'), 500
    return render_template('json_review.html', json_data=None)

@app.route('/index2')
def mainpage():
    return render_template('index2.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/regular_content')
def regular_content():
    return render_template('regular_content.html')


if __name__ == '__main__':
    app.run(debug=True)