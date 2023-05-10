from flask import Flask, request, render_template,send_file

from data.plot_data import createPlot
from data.qa_data import cleanReport
from report.export import cleanE
from report.summary import cleanS

app = Flask(__name__)
app.use_static_for = 'static'

ALLOWED_EXTENSIONS = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                cleanReport(file)
                createPlot()
                return send_file('SCS_QA.xlsx', as_attachment=True)

        elif 'Summary' in request.files:
            file = request.files['Summary']
            if allowed_file(file.filename):
                cleanS(file)
                return send_file('Summary.xlsx', as_attachment=True)

        elif 'Report' in request.files:
            file = request.files['Report']
            if allowed_file(file.filename):
                cleanE(file)
                return send_file('Report.xlsx', as_attachment=True)

        return render_template('error.html')

    return render_template('index.html')

def main():
    upload_file()

if __name__ == '__main__':
    app.run(debug=True)
    main()