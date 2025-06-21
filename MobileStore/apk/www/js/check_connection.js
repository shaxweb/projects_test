
if (navigator.offline) {
  window.location.assign("../main/connect_error.html");
}

window.addEventListener("offline", () => {
  window.location.assign("../main/connect_error.html");
});

fetch("https://somestore.onrender.com/")
.then(response => {})
.catch(error => {
  alert(error.message)
  window.location.assign("../main/connect_error.html")
})
