
if (navigator.offline) {
  window.location.assign("main/connect_error.html");
}

window.addEventListener("offline", () => {
  window.location.assign("main/connect_error.html");
});

fetch("https://somestore.onrender.com/")
.then(response => {})
.catch(error => {
  window.location.assign("main/connect_error.html")
})
