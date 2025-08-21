import os
import requests

WEBHOOK_URL = os.getenv("DOORAY_INCOMING_URL")
BOT_NAME = "나는봇"
BOT_ICON = "https://static.dooray.com/static_images/dooray-bot.png"
TEXT = "안녕하세요. 나는봇입니다."

payload = {
    "botName": BOT_NAME,
    "botIconImage": BOT_ICON,
    "text": TEXT
}
headers = {"Content-Type": "application/json"}

resp = requests.post(WEBHOOK_URL, json=payload, headers=headers)

print("Status:", resp.status_code)
print("Response text:", resp.text)   # 응답 본문 확인
