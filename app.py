import flask
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


@app.route("/medicacao/<nome_medicacao>")
def medicacao(nome_medicacao):
    return render_template("medicacao.html", nome_medicacao=nome_medicacao)


if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#commit