from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
render = render_template
CORS(app)

users = []


@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify({"status": True, "message": "Hello, World!", "data": users})


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.json
        username, password = data.get("username"), data.get("password")
        
        if username and password:
            users.append({"username": username, "password": password})
            return jsonify({"status": True, "message": "Added"})
        else:
            return jsonify({"status": False, "message": "Uncorrect datas"})
        
    return jsonify({"status": True, "message": "User created"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)