from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e28357226359d27d44bd4.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e28357226359d27d44bd4.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAM_X_ALPHA")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_X_ALPHA_NETWORK")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2131967391").split()))


FAILED = "https://telegra.ph/file/e28357226359d27d44bd4.jpg"
