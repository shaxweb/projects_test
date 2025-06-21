import requests

BOT_TOKEN = "8158445939:AAHmoesq6Em6F5QdxcNhRJYSVL2pTLpUyn0"
CHAT_ID = 6181120570

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Пример использования
# send_message("Hello from requests!")