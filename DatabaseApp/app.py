from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json 

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)