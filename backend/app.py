from flask import Flask, render_template, request, jsonify
from model_loader import get_response   # our prediction function

# Flask app – point to frontend folders
app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend/static"
)

@app.route("/")
def home():
    """Serve the main chat interface."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle chat messages from the frontend.
    Expects JSON: { "message": "user text" }
    Returns JSON: { "reply": "bot response" }
    """
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message."}), 400

    user_msg = data["message"].strip()
    if not user_msg:
        return jsonify({"reply": "Message cannot be empty."}), 400

    # Get bot response (handles low-confidence internally)
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)