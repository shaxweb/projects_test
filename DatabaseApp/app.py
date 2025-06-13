from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, sql

app = Flask(__name__)
render = render_template
CORS(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        user = {"username": data.get("username"), "password": data.get("password")}
        sql.register(user["username"], user["password"])
        return jsonify({"status": True, "message": "Successfully Saved!"})
        
    return render("index.html", name="Shaxrux")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)