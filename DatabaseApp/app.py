from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, bot

app = Flask(__name__)
render = render_template
CORS(app)

users = []


@app.route("/", methods=["GET", "POST"])
def home():
    global users
    if request.method == "POST":
        data = request.json
        user = data["user"]
        users.append({"user": user, "lat": data["lat"], "lng": data["lng"]})
        
        return jsonify({"status": True, "message": "Thanks"})

    return render("index.html", name="Shaxrux", users=users)


@app.route("/smtb/", methods=["GET", "POST"])
def smtb_func():
    if request.method == "POST":
        data = request.json
        message = data.get("message")
        if message:
            bot.send_message(message)
            return jsonify({"status": True, "message": "Message sended!"})
        else:
            return jsonify({"satuts": False, "message": "Enter the text"})
    
    return render("index.html", name="SMTB")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)