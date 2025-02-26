from flask import Flask, request, jsonify
import requests
import os

app1 = Flask(__name__)

# Get Hugging Face API key from environment variable
HF_API_KEY = os.getenv("HF_API_KEY")

# Hugging Face API URL for Mistral-7B
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"

@app.route("/")
def home():
    return "AI Tutor API is Running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(HF_API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get response", "details": response.text}), 500

if __name__ == "__main__":
    app1.run(debug=True)
