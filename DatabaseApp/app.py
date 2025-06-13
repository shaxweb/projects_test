from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "GET":
	  return jsonify({"status", True; "message": "Hello, World!"})
	
	elif request.method == "POST":
	  data = request.json
	  with open("datas.json", "w") as file:
	    file.write(data)
	  return jsonify({"status": True, "message": "Saved!"})
	

if __name__ == '__main__':
    app.run(debug=True)