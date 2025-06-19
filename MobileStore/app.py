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


@app.route("/search/")
def search():
    query = request.args.get("q")
    
    if query:
        products = sql.get_all_data()["products"]
        data = scripts.search_products(query.lower(), products)
        return jsonify({"status": True, "message": "ul", "data": data})
    return jsonify({"status": True, "message": "Hello, World"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)