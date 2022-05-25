import flask
import os, bs4
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)
url = 'https://www.google.com/webhp?hl=pt-BR&sa=X&ved=0ahUKEwjKtIiHt_v3AhXNFbkGHa7XAm8QPAgI'

@app.route("/", methods=["GET", "POST"])
def homepage():
    remedio = ""
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        numero = 0



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