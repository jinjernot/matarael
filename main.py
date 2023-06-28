from flask import Flask, request, render_template, send_file
from data.plot_data import generate_plot
from data.qa_data import clean_report 
from data.qa_granular import clean_granular

# Create a Flask application object.
app = Flask(__name__)

# Get files from the `static` directory.
app.use_static_for = 'static'

# Allowed file extensions for the uploaded file.
VALID_FILE_EXTENSIONS = {'xlsx', 'xlsm', 'csv', "json"}

# Check if a file has a valid extension.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in VALID_FILE_EXTENSIONS

# Check if the file has a valid extension, it is processed by the appropriate function, and the results are returned. Otherwise, return an error.
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'Regular' in request.files:
            file = request.files['Regular']
            try:
                if allowed_file(file.filename):
                    clean_report(file)
                    #generate_plot()
                    return send_file('SCS_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')

        elif 'Granular' in request.files:
            file = request.files['Granular']
            try:
                if allowed_file(file.filename):
                    clean_granular(file)
                    return send_file('SCS_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')
            
        elif 'JSON' in request.files:
            file = request.files['JSON']
            try:
                if allowed_file(file.filename):
                    filename = file.filename
                    file.save('json/' + filename)  # Save the file to the 'json' folder
                    return 'File uploaded successfully!'
            except Exception as e:
                print(e)
                return render_template('error.html')

        return render_template('error.html')       
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
