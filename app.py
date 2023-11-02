from flask import Flask, render_template, request
import openai
import os


# ChaveOpenai = os.getenv("OpenaiKey")

app = Flask(__name__)

# openai.api_key = ChaveOpenai
openai.api_key = '*'

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
    
    if completion.choices(0).mensage is not None:
        return completion.choices(0).message
    else:
        return 'Falha para geração da resposta!'
    
if __name__== '__main__':
    app.run()

    
  