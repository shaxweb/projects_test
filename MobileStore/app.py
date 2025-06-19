from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import scripts, json, sql

app = Flask(__name__)
render = render_template
CORS(app)


@app.route("/")
def home():
    products = sql.get_all_data()["products"]
    return jsonify({"status": True, "message": "Hello, Wolrd", "data": products})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)