from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json 

app = Flask(__name__)
render = render_template
CORS(app)

users = []


@app.route("/", methods=["GET", "POST"])
def home():
    global coords
    if request.method == "POST":
        data = request.json
        user = data["user"]
        new_users = []
        for i in users:
            if i["user"] == user:
                new_users.append({"user": user, "lat": data["lat"], "lng": data["lng"]})
                continue
            new_users.append(i)
        users = new_users
        
        return jsonify({"status": True, "message": "Thanks"})

    return render("index.html", name="Shaxrux", coords=coords)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)