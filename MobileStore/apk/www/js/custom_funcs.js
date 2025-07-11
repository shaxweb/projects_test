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

const customDismissalBox = (message) => {
  let dismissalBox = document.createElement("div")
  dismissalBox.className = "customDismissalBox"
  dismissalBox.innerText = message
  document.body.appendChild(dismissalBox)
  setTimeout(() => {dismissalBox.style.display = "none"}, 5000)
}