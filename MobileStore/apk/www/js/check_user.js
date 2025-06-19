let db = localStorage;

let cur_user = JSON.parse(db.getItem("cur_user")) || null

if (cur_user == null) {window.location.replace("../login.html")}