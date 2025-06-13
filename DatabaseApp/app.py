from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
render = render_template
CORS(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = requests.json
        return jsonify({"status": True, "message": f"Thanks for {data}"})
    return render("index.html", name="Shaxrux")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)