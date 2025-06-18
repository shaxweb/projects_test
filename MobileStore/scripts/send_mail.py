import smtplib, secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shaxrux243@gmail.com"
sender_password = "ojfb hvou npgr qfhi"  # Используйте пароль приложения, а не обычный!


def send_token_to_mail(receiver_email):
  token = secrets.token_hex(16)
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = "Регистрация!"
  body = f"Ваш ссылка => https://shaxweb-database.onrender.com/register?token={token}"
  message.attach(MIMEText(body, "plain"))
  
  try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login(sender_email, sender_password)
      server.sendmail(sender_email, receiver_email, message.as_string())
      server.quit()
      # print("Письмо успешно отправлено!")
  except Exception as e:
      # print(f"Ошибка при отправке: {e}")