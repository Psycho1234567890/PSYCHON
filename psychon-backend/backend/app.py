from flask import Flask, request, jsonify
from flask_cors import CORS
from model_loader import get_response

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message."}), 400
    user_msg = data["message"].strip()
    if not user_msg:
        return jsonify({"reply": "Message cannot be empty."}), 400
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)