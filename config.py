from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/Bilmem-04-28")
START_IMG = getenv("START_IMG", "https://telegra.ph/Bilmem-04-28")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sehrinanem")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/muzik_kolik")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/Bilmem-04-28"
