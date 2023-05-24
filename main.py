from flask import Flask, request, render_template,send_file

from data.plot_data import createPlot
from data.qa_data import cleanR
from data.granular import cleanG
from report.export import cleanE
from report.summary import cleanS
from database.mongo import connect

app = Flask(__name__)
app.use_static_for = 'static'


ALLOWED_EXTENSIONS = {'xlsx'}

@app.route('/mongo')
def mongo():
    connect()
    collection = connect()
    return render_template('mongo.html', collection=collection)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'Regular' in request.files:
            file = request.files['Regular']
            try:
                if allowed_file(file.filename):
                    cleanR(file)
                    createPlot()
                    return send_file('SCS_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')
            
        elif 'Granular' in request.files:
            file = request.files['Granular']
            try:
                if allowed_file(file.filename):
                    cleanG(file)
                    return send_file('Atom_QA.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')

        elif 'Summary' in request.files:
            file = request.files['Summary']
            try:
                if allowed_file(file.filename):
                    cleanS(file)
                    return send_file('Summary.xlsx', as_attachment=True)
            except Exception as e:
                print(e)
                return render_template('error.html')

        elif 'Report' in request.files:
            file = request.files['Report']
            try:
                if allowed_file(file.filename):
                    cleanE(file)
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