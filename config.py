from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "130"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/httptelegraph55-03-30-15-04-09")
START_IMG = getenv("START_IMG", "https://telegra.ph/Guzel-03-30")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sehrinanem")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mehmetttbio")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/httptelegraph55-03-30-15-04-09"
