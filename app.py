from flask import Flask, render_template, request
import openai
import os


# Recupere o valor da variável de ambiente
ChaveOpenai = os.getenv("OpenaiKey")

# Verifique se a variável de ambiente foi definida
# if ChaveOpenai is not None:
#     print(f"O valor da variável de ambiente OpenaiKey é: {ChaveOpenai}")
# else:
#     print("A variável de ambiente OpenaiKey não está definida.")

app = Flask(__name__)

openai.api_key = ChaveOpenai

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])

def api():
    menssage = request.json.get("message")
    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente de programação."},
        {"role": "user", "content": menssage},
    ]
    )
    
    if completion.choices(0).mensage!=None:
        return completion.choices(0).message
    else:
        return 'Falha para geração da resposta!'
    
    if __name__=='__main__':
        app.run()