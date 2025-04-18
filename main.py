import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import pytz
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def get_gold_price():
    today_price = 3475
    avg_30_day = 3498
    return today_price, avg_30_day

def build_message(today, avg):
    result = "✅ 低於平均" if today < avg else "❌ 高於平均"
    return f"""【黃金快報】
日期：{datetime.now(pytz.timezone("Asia/Taipei")).strftime('%Y/%m/%d')}
每公克價格：NT${today}
30 天平均價：NT${avg}
結果：{result}
"""

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def send_email(msg):
    message = MIMEText(msg)
    message["Subject"] = "黃金快報"
    message["From"] = EMAIL_USER
    message["To"] = EMAIL_RECEIVER
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(message)

def main():
    today, avg = get_gold_price()
    msg = build_message(today, avg)
    send_telegram(msg)
    send_email(msg)
    print("通知已發送")

if __name__ == "__main__":
    main()
