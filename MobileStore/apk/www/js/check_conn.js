
if (navigator.offline) {
  window.location.assign("main/connect_error.html");
}

window.addEventListener("offline", () => {
  window.location.assign("main/connect_error.html");
});

fetch("https://shaxweb-database.onrender.com/")
.then(response => {})
.catch(error => {
  console.log(error.message)
  window.location.assign("main/connect_error.html")
})
