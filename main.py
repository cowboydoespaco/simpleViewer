# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os, Image

app = Flask(__name__)
app.config.from_pyfile('main.cfg')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

db = SQLAlchemy(app)

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    nomeArquivo = db.Column(db.String(50))
    
    def __init__(self, titulo, nomeArquivo):
        self.titulo = titulo
        self.nomeArquivo = nomeArquivo

    def __repr__(self):
        return '<Imagem: %r>' % self.titulo

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
        salvarImagem(file, request.form['titulo'], file.filename)
        flash(u'Sua foto foi enviada com sucesso.', 'alert-success')
        return redirect('/')
    else:
        flash(u'Tipo de arquivo não permitido.', 'alert-error')
        return redirect('/')

def salvarImagem(file, titulo, nomeArquivo):
    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)
    generateThumbnail(save_path, "thumb_"+filename)
    imagem = Imagem(secure_filename(request.form['titulo']), filename)
    db.session.add(imagem)
    db.session.commit()

def generateThumbnail(save_path, thumb_name):
    im = Image.open(save_path)
    im.thumbnail((100,100))
    im.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb_name))

if __name__ == "__main__":
    app.run()