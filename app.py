from flask import Flask, render_template, request
import openai
import os

import json
from flask import jsonify


ChaveOpenai = os.getenv("OpenaiKey")

app = Flask(__name__)

openai.api_key = ChaveOpenai

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])

def api():
    message = request.json.get("message")
    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    
    messages=[
        {"role": "system", "content": "Você é um assistente de programação."},
        {"role": "user", "content": message},
    ]
    )
    
    if completion.choices[0].message is not None:
        response_data = {
            "content": completion.choices[0].message['content']
        }
        return jsonify(response_data)
    else:
        response_data = {
            "error": "Falha para geração da resposta!"
        }
        return jsonify(response_data)

    
if __name__=='__main__':
    app.run()

    
  