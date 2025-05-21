from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configura tu API Key (debes definirla en Render como variable de entorno)
API_KEY = os.getenv("API_KEY")

# Configurar el acceso a la API de Gemini
genai.configure(api_key=API_KEY)

# Instanciar el modelo de Gemini
model = genai.GenerativeModel("gemini-1.5-flash-latest")

@app.route("/chat", methods=["GET"])
def chat():
    prompt = request.args.get("prompt")
    
    if not prompt:
        return jsonify({"error": "Falta el parámetro 'prompt'"}), 400

    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
