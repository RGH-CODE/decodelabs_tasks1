from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not data:
        data = request.form.to_dict() or request.values.to_dict()

    user_message = data.get("message", "")
    user_name = data.get("user_name", "")

    if not user_message:
        return jsonify({
            "response": "I did not receive your message. Please try again."
        })

    print("User:", user_message)

    try:
        response = get_response(user_message, user_name)
    except Exception as e:
        print("Chatbot error:", e)
        response = "Sorry, I could not process your request."

    print("Bot:", response)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)