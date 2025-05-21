from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Leer la API Key desde variable de entorno
API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input
    )
    return jsonify({"reply": response.text})

@app.route('/')
def home():
    return "Cachimbot API activa."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)