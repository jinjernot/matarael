from flask import Flask, request, render_template,send_file

from data.plot_data import createPlot
from data.qa_data import cleanReport
from data.qa_granular import cleanGranular
from report.export import cleanExport
from report.summary import cleanSummary
#from database.mongo import connect

# Create a Flask application object.
app = Flask(__name__)

# Get files from the `static` directory.
app.use_static_for = 'static'

# Allowed file extensions for the uploaded file.
ALLOWED_EXTENSIONS = {'xlsx'}

# Connect to a MongoDB database and return a collection object.
#@app.route('/mongo')
#def mongo():
#    connect()
#    collection = connect()
#   return render_template('mongo.html', collection=collection)

# Check if a file has a valid extension.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Check if the file has a valid extension, it is processed by the appropriate function and the results are returned. Otherwise, return an error.
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'Regular' in request.files:
            file = request.files['Regular']
            try:
                if allowed_file(file.filename):
                    cleanReport(file)
                    createPlot()
                    return send_file('SCS_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')
            
        elif 'Granular' in request.files:
            file = request.files['Granular']
            try:
                if allowed_file(file.filename):
                    cleanGranular(file)
                    return send_file('SCS_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')

        elif 'Summary' in request.files:
            file = request.files['Summary']
            try:
                if allowed_file(file.filename):
                    cleanSummary(file)
                    return send_file('Summary.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')

        elif 'Report' in request.files:
            file = request.files['Report']
            try:
                if allowed_file(file.filename):
                    cleanExport(file)
                    return send_file('Report.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')
        return render_template('error.html')
    return render_template('index.html')

def main():
    upload_file()

if __name__ == '__main__':
    app.run(debug=True)
    main()