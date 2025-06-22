const customAlert = (message) => {
  let alertContainer = document.createElement("div")
  let alertBox = document.createElement("div")
  alertContainer.className = "customAlertContainer"
  alertBox.className = "customAlertBox"
  alertBox.innerHTML = `<h1>${message}</h1>`
  alertContainer.onclick = () => {alertContainer.style.display = "none"}
  
  alertContainer.appendChild(alertBox)
  document.body.appendChild(alertContainer)
}