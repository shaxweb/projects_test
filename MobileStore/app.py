from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, bot

app = Flask(__name__)
render = render_template
CORS(app)

users = []


@app.route("/", methods=["GET", "POST"])
def home():
    return render("index.html")


@app.route("/register/", method=["GET"])
def register():
  return jsonify({"status": True, "message": f"Datas: {request}"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)