import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")

# Aishu
#API_ID = int(getenv("API_ID", "8045459"))
#API_HASH = getenv("API_HASH", "e6d1f09120e17a4372fe022dde88511b")
#BOT_TOKEN = getenv("BOT_TOKEN", "7068876137:AAEO6UXBfVcj9BMPXsbdAgApCntlXmYjNTw")
#STRING_SESSION = getenv("STRING_SESSION", "BQDMBnkAYiOVd1XgRlwY7fGlRrmYnn79K2KzLfsXiVAFVRYYfmTzSslg4VMO9zi3V-8UvChSAZJiu4OFnNCHnFYKstELWLGKF4KW70ml64zlF8mgCnAtUPDvJXpJtgrIcjZr-ieZAgda99Giv_ivVbh2V5wLqgSYUbSZ_GKGM4usnJvQFZg6YGMoTMWKQPuZhxphI74-_PyXED5xHpoYpBjbaw00wy8RKJzw3e_NMpXwID5Io1P2uBlx9vbmLcJMHO7DK4YvwsCXQUBNhskfzSiWQqpcVH_eZEW2NN-1uWKDsWbVZPY4PDjraaBVhF5rOi_MVx4oBTAzCV1hT2BGsljeQb7AAAAAEyRzmXAA")
#MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
#LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))

# Rajesh
API_ID = int(getenv("API_ID", "13371001"))
API_HASH = getenv("API_HASH", "f9e4a79850af44c26d736453a95308fc")
BOT_TOKEN = getenv("BOT_TOKEN", "6773882212:AAGxTyLGiKX-8syKmtgRbHD4Jn5NTiem0DA")
STRING_SESSION = getenv("STRING_SESSION", "BQB6w5MAddViqx9rSNWBXf1cB8ZgULzrG5yV4Z_Sde9zCtjuCbJVgucg9F3RK6Uq3x4gx22eGYfxOpE_HLivLvPjB6YVg7hGE2pTayMQKjH9KgausKH0cgiTFVrHJ_FHMZb9PFjFvZayLO6VJSihWzULveYiPqisp2SH8rxxv5eTKRgA5WOYc5whgZgQPU2BDI8aaq4axZT1Q5KOgeR7dRpj0oHNzL4eEECDGzdojhr3In0DK5KYjFd1waxL6HxYobLQL7iX4iSGBrStt7TtJnQYavXnLN6Z1kXE7rpNaBe-TZnTl9XDtc2Cb1wt47mg2NernwQ_H_2mvrWk-_dDxXswgi0AIAAAAABMXtJJAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002063555777"))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\nʜᴇʏ ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭\n\n☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\n➽─────────────────❥\n\n💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋\n https://t.me/HeartBeat_Muzic \n\n➽─────────────────❥\n\n😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ, ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ..\nʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏʙʟᴏᴄᴋ (ᴜᴘᴛᴏ 3 ᴍᴇꜱꜱᴀɢᴇꜱ)\n\n**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 3))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/9ee37cccd7bf55c3ec953.png")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Genius")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

