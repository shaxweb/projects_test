from flask import Flask, jsonify, request
import json

app = Flask(__name__)
have = 0


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return jsonify({"status": True, "message": "Hello, World!"})  # ✅ исправлено

    elif request.method == "POST":
        data = request.json
        with open("datas.json", "w") as file:
            json.dump(data, file, indent=4)  # ✅ записываем как JSON, а не просто text
        return jsonify({"status": True, "message": "Saved!"})


@app.route("/api/users/", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        if have == 1:
            with open("users.json", "r") as file:
                data = file.read()
                return jsonify({"sended": data})
    
        else:
            with open("users.json", "w") as file:
                json.dump([], file, indent=4)
            return jsonify({"status": True})
    elif request.method == "POST":
        data = request.json
        users = []
        with open("users.json", "r") as file:
            users = file.read()
        users.append(data)
        with open("users.json", "w") as file:
            file.write(users, file, indent=4)
        
        return jsonify({"status": True})
                

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)