import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "26715173"))
API_HASH = os.getenv("API_HASH", "e208f4ac326676f273054f2095211fea")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7697479557:AAG2pYNsXfbM_SqOT2BqSMBodmaYmnhVEl4")
OWNER_ID = int(os.getenv("OWNER_ID", "7946875913"))
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Likhith:Likhithbots@likhith.jm3wayg.mongodb.net/?retryWrites=true&w=majority&appName=likhith")
