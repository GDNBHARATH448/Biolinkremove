import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "29896633"))
API_HASH = os.getenv("API_HASH", "7a8a6dd1c08f6ffc33645885bb3ecf77")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7697479557:AAGSYiTMd4biFnLw_rfJ-heLgIQYIOn53VQ")
OWNER_ID = int(os.getenv("OWNER_ID", "5867783630"))
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Likhith:Likhithbots@likhith.jm3wayg.mongodb.net/?retryWrites=true&w=majority&appName=likhith")
