from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    template = 'index.html'
    return render_template('base.html', **locals())

@app.route("/requisicao/", methods=['GET', 'POST'])
def requisicao():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return str(file.filename + ' saved')
    # return 'got it.'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')