from flask import Flask, jsonify, request
import json  # для сериализации данных в JSON

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return jsonify({"status": True, "message": "Hello, World!"})  # ✅ исправлено

    elif request.method == "POST":
        data = request.json
        with open("datas.json", "w") as file:
            json.dump(data, file, indent=4)  # ✅ записываем как JSON, а не просто text
        return jsonify({"status": True, "message": "Saved!"})

if __name__ == '__main__':
    app.run(debug=True)