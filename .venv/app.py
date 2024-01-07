from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configuracion de credenciales de la API de OpenAI
openai.api_key = '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'

# Define la ruta predeterminada para volver al inicio
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

# Define la ruta /api para manejar requests de tipo GET y POST
@app.route("/api", methods=["POST", "GET"])
def api():
    # Recibe el mensaje de la peticion
    message = request.json.get("message")

    # Envia el mensaje a traves de la API de OpenAI y recibe la respuesta

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "user", "content": message}
        ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    
    else:
        return 'Failed to Generate response!'
    
if __name__=='__main__':
    app.run()