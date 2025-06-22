from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, secrets, difflib

sender_email = "shaxrux243@gmail.com"
sender_password = "ojfb hvou npgr qfhi"  # Используйте пароль приложения, а не обычный!


def send_token_to_mail_old(receiver_email):
  token = secrets.token_hex(16)
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = "Регистрация!"
  body = f"Ваш ссылка => https://somestore.onrender.com/auth?token={token}"
  message.attach(MIMEText(body, "plain"))
  
  try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login(sender_email, sender_password)
      server.sendmail(sender_email, receiver_email, message.as_string())
      server.quit()
      return token
      # print("Письмо успешно отправлено!")
  except Exception as e:
      print(f"Ошибка при отправке: {e}")


def send_mail_register_log(username, user_mail):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = "shaxrux243@gmail.com"
    message["Subject"] = "Регистрация!"
    body = f"New User registered. Username: {username} and mail: {user_mail}"
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return token
      # print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")


def search_products(query, products):
    results = []

    for row in products:
        title = row[1].lower()
        description = row[2].lower()
        if query in title or query in description:
            results.append(row)
        else:
            matches = difflib.get_close_matches(query, [title], cutoff=0.6)
            if matches:
                results.append(row)

    return results


def send_token_to_mail(username, user_mail):
    token = secrets.token_hex(16)
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = user_mail
    message["Subject"] = "Подтверждение аккаунта"

    # Загружаем HTML-шаблон из файла
    with open("templates/send_mail.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    # Подставляем переменные в шаблон
    html_body = html_template.replace("{{TOKEN_LINK}}", f"https://somestore.onrender.com/auth?token={token}")

    # Создаём MIME объект
    mime_html = MIMEText(html_body, "html")
    message.attach(mime_html)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_mail, message.as_string())
        server.quit()
        return {"status": True, "token": token}
    except Exception as e:
        return {"status": False, "error": e}