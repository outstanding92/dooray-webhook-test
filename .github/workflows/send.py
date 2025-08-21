import os
import requests

WEBHOOK_URL = os.getenv("DOORAY_INCOMING_URL")  # GitHub Secrets에서 불러오기
BOT_NAME = "자동봇"
BOT_ICON = "https://static.dooray.com/static_images/dooray-bot.png"
TEXT = "안녕"

payload = {
    "botName": BOT_NAME,
    "botIconImage": BOT_ICON,
    "text": TEXT
}
headers = {"Content-Type": "application/json"}

resp = requests.post(WEBHOOK_URL, json=payload, headers=headers)
print(resp.status_code, resp.text)
