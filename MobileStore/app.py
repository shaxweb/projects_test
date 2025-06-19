from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import scripts, json, sql

app = Flask(__name__)
render = render_template
CORS(app)


@app.route("/")
def home():
    print("\n\n\nHello, Wolrd!\n\n\n")
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


@app.route("/get_user/")
def get_user():
    data = request.args
    username = data.get("username")
    if username:
        user = sql.get_user_by_username(username)
        if user:
            return jsonify({"status": True, "id": user[0], "username": user[1], "password": user[3]})
    
    return jsonify({"status": False})


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.data
        username, email, password = data.get("username"), data.get("email"), data.get("password")
        
        if not sql.get_user_by_username(username):
            if not sql.get_user_by_email(email):
                sql.create_wait_user(username, email, password)
                scripts.send_token_to_mail(email)
                return jsonify({"status": True, "message": "Token sended"})
            return jsonify({"status": False, "error": "email"})
        return jsonify({"status": False, "error": "username"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)