# import flask
from flask import Flask, render_template, request
import openai

app = flask(__name___)

openai.api_key = "*"

@app.rout("/")

def index():
    return render_template(index.html)

@app.route("/api", methods=["POST"])

def api():
    menssage = request.json.get("message")
    completion = openai.ChatCompletion.creat(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente de programação."},
        {"role": "user", "contente": menssage},
    ]
    )
    
    if completion.choices(0).mensage!=Nome:
        return completion.choices(0).message
    else:
        return 'Falha para geração da resposta!'
    
    if __name__=='__main__':
        app.run()