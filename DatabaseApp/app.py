from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json 

app = Flask(__name__)
render = render_template
CORS(app)

coords = []


@app.route("/", methods=["GET", "POST"])
def home():
    global coords
    if request.method == "POST":
        data = request.json
        coords.append(data)
        return jsonify({"status": True, "data": data})
        
    return render("index.html", name="Shaxrux", coords=coords)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)