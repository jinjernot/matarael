from flask import Flask, request, render_template, send_from_directory, abort
from data.qa_data import clean_report
import config

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

if __name__ == '__main__':
    app.run(debug=True)
