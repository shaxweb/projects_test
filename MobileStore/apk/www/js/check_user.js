let db = localStorage;

let cur_user = JSON.parse(db.getItem("cur_user")) || null

if (cur_user == null) {window.location.replace("../login.html")}
else {
  let user_id = cur_user["id"]

  fetch(`https://somestore.onrender.com/get_user/?id=${user_id}`)
  .then(response => response.json())
  .then(data => {
    if (!data.status) {
      window.location.replace("../login.html")
    }
  })
}