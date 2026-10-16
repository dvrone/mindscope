import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi. .env faylini tekshiring.")

# ADMIN_ID ixtiyoriy: berilmasa /stats hech kimga ishlamaydi
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
