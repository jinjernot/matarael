from flask import Flask, request, render_template, send_file
from data.plot_data import generate_plot
from data.qa_data import clean_report 

app = Flask(__name__)
app.use_static_for = 'static'

VALID_FILE_EXTENSIONS = {'xlsx', 'xlsm', 'csv', "json"}
VALID_PASSWORD = "123"

def is_valid_password(password):
    return password == VALID_PASSWORD

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in VALID_FILE_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        password = request.form.get('password')  # Get the password from the form input
        if is_valid_password(password):
            return render_template('index2.html')  # Load index2.html if the password is valid
        else:
            return render_template('error password.html')
    return render_template('index.html')


@app.route('/upload-file', methods=['POST'])
def process_file():
    if 'Regular' in request.files:
        file = request.files['Regular']
        try:
            if allowed_file(file.filename):
                clean_report(file)
                return send_file('SCS_QA.xlsx', as_attachment=True)
        except Exception as e:
            print(e)
            return render_template('error.html')

    elif 'JSON' in request.files:
        file = request.files['JSON']
        try:
            if allowed_file(file.filename):
                filename = file.filename
                file.save('/home/garciagi/SCS_Tool/json/' + filename)
                return render_template('file_uploaded.html')
        except Exception as e:
            print(e)
            return render_template('error.html')

    return render_template('error.html')  # Display the error page if none of the upload conditions are met

if __name__ == '__main__':
    app.run(debug=True)
