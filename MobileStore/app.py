from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
render = render_template
CORS(app)

users = []


@app.route("/", methods=["GET", "POST"])
def home():
    return render("index.html")


@app.route("/register/", methods=["GET"])
def register():
    data = request.args
    username, password = data.get("username"), data.get("password")
    if not username:
        return jsonify({"status": False, "message": "Username must not be empty"})
    if not password:
        return jsonify({"status": False, "message": "Password must not be empty"})
    
    for i in users:
        if i["username"] == username:
            return jsonify({"status": False, "message": "Username already taked"})
    
    users.append({"username": username, "password": password})
    
  return jsonify({"status": True, "message": f"Datas: {request}"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)