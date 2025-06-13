from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
render = render_template
CORS(app)


@app.route("/")
def home():
    # if request.method == "GET":
        # return jsonify({"status": True, "message": "Hello, World"})
    return render("index.html", name="Shaxrux")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)