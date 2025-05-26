from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/")
def index():
    return render_template("index.html", project_name="ChatOnline.Solutions")

@app.route("/api/ask", methods=["POST"])
def ask():
    user_input = request.json.get("prompt", "")
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"Server error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
