# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config.from_pyfile('main.cfg')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
db = SQLAlchemy(app)

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
        alert_type = 'alert-success'
        flash(u'Sua foto foi enviada com sucesso.')
    else:
        alert_type = 'alert-error'
        flash(u'Tipo de arquivo não permitido.')

    template = 'index.html'
    return render_template('base.html', **locals())

if __name__ == "__main__":
    app.run()