import os
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.environ.get("BOT_TOKEN")
USERNAME = os.environ.get("BOT_USERNAME")
IPADDR = os.environ.get("IPADDR")
