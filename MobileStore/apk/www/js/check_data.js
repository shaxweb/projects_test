const check_username = (username) => {
  const symbols = Array.from("qwertyuiopasdfghjklzxcvbnm1234567890_");
  
  if (username.length < 6) { return {status: false, message: "len error"} }
  if (username.includes(" ")) { return {status: false, message: "without space"} }
  for (let i of username) {
    if (!symbols.includes(i.toLowerCase())) { return {status: false, message: `error with ${i}`} }
  }
  return {status: true, message: "done"}
}

const check_passord = (password1, password2) => {
  if (password1.length < 8) { return {status: false, message: "len error"} }
  if (password1 == password2) { return {status: true, message: "done"} }
  else { return {status: false, message: "error not match"} }
}

const check_mail = (mail) => {
  if (!mail.includes("@gmail.com")) { return {status: false, message: "uncorrect mail"} }
  return {status: true, message: "done"}
}

