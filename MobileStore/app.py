from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import database
import scripts
import bot

app = Flask(__name__)
render = render_template
CORS(app)
images_path = "images"


@app.route("/")
def home():
    data = database.get_all_data()
    return jsonify({"status": True, "message": "Hello, Wolrd", "data": data})


@app.route("/search/")
def search():
    query = request.args.get("q")
    
    if query:
        products = database.get_all_data()["products"]
        data = scripts.search_products(query.lower(), products)
        return jsonify({"status": True, "message": "ul", "data": data})
    return jsonify({"status": True, "message": "Hello, World"})


@app.route("/get_user/")
def get_user():
    data = request.args
    username = data.get("username")
    user_id = data.get("id")
    if username:
        user = database.get_user_by_username(username)
        if user:
            return jsonify({"status": True, "user": {"id": user[0], "username": user[1], "password": user[2], "mail": user[3]}})
        else:
            return jsonify({"status": False})
    
    elif user_id:
        user = database.get_data(user_id)["user"]
        if user:
            return jsonify({"status": True, "user": {"id": user[0], "username": user[1], "password": user[2], "mail": user[3]}})
        else:
            return jsonify({"status": False})

    return jsonify({"status": False})


@app.route("/get_product/")
def get_product():
    product_id = request.args.get("product_id")
    if product_id:
        product = database.get_data(product_id)["product"]
        if product:
            return jsonify({"status": True, "product": product})
        else:
            return jsonify({"status": False, "message": "product not found"})
    return jsonify({"status": False})


@app.route("/get_products/")
def get_products():
    data = request.args.get("products")
    products = {}
    if data:
        for i in data:
            product = database.get_data(i)["product"]
            if product:
                if products.get(f"product_{i}"):
                    products[f"product_{i}"]["quantity"] += 1
                else:
                    products[f"product_{i}"] = {"quantity": 1, "data": product}
    
    return jsonify({"status": True, "data": products})


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.get_json()
        username, email, password = data.get("username"), data.get("email"), data.get("password")
        
        if not database.get_user_by_username(username):
            if not database.get_user_by_email(email):
                token = scripts.send_token_to_mail(username, email)
                if token["status"]:
                    database.create_wait_user(username, email, password, token["token"])
                    return jsonify({"status": True, "message": "Token sended"})
                else:
                    bot.send_message(f"error: {token["error"]}")
                    return jsonify({"status": False})
            return jsonify({"status": False, "error": "email"})
        return jsonify({"status": False, "error": "username"})
    return jsonify({"status": True})


@app.route("/auth/")
def auth_func():
    data = request.args
    token = data.get("token")
    if token:
        user = database.get_wait_user_by_token(token)
        if user:
            bot.send_message(f"SomeStoreLog: {user}")
            database.create_user(user[1], user[3], user[2])
            database.delete_wait_user(user[0])
            scripts.send_mail_register_log(user[1], user[3])
            return render("auth.html", status=True, username=user[1])
    
    return render("auth.html", status=False, error="Token was broken", data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)