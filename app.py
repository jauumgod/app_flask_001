from flask import Flask, url_for, render_template, redirect,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']='my-secret-key@'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask_app01.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(184))
    password = db.Column(db.String(184))

    # def __init__(self,nome,password):
    #     self.nome = nome
    #     self.password = password
    
    def __str__(self):
        return self.name


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/postagens")
def postagens():
    return render_template("postagens.html")

#TODO: create Login

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        r = User()
        r.usuario = request.form['usuario']
        r.senha = request.form['senha']
        db.session.add(r)
        db.session.commit()

        return redirect(url_for('index')) #redirect temp

    return render_template("register.html")


@app.route("/usuarios")
def usuarios():
    usuarios = User.query.all()
    return render_template("usuarios.html",users=usuarios)

if __name__=="__main__":
    app.run(debug=True)