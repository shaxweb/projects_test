from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, sql

app = Flask(__name__)
render = render_template
CORS(app)

coords = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        coord = {"lat": data.lat, "lng": data.lng}
        coords.append(coord)
        return jsonify({"status": True})
        
    return render("index.html", name="Shaxrux", coords=coords)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)