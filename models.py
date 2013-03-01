from main import db

##########################################

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    nomeArquivo = db.Column(db.String(50))
    
    def __init__(self, titulo, nomeArquivo):
        self.titulo = titulo
        self.first_name = first_name

    def __repr__(self):
        return '<Imagem: %r>' % self.titulo