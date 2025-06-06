import os
from os import getenv

API_ID = int(os.environ.get("21283957", ""))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("aade44a828de52da2a6ef816b120020b", "")
BOT_TOKEN = os.environ.get("7902772572:AAHsBU25TDn-GUGa9MXui0gR2pIw7LNB82I", "")

OWNER_ID = int(os.environ.get("6917342289", ""))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("2059887634", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
