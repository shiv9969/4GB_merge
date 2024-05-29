import os

class Config(object):
    API_HASH = os.environ.get("API_HASH", "cbabdb3f23de6326352ef3ac26338d9c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "9301087")
    OWNER = os.environ.get("OWNER", "1525203313")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "t.me/assaulter_shiv")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "bob_files1")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Shivji:BoBfiles@cluster0.t1mka5v.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOG_CHANNEL", "-1002218617951")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    UPSTREAM_REPO = "https://github.com/shiv9969/4GB_merge"
    UPSTREAM_BRANCH = "master"

    START_TEXT = """
Hɪ 👋 I Aᴍ A Fɪʟᴇ/Vɪᴅᴇᴏ Mᴇʀɢᴇ Bᴏᴛ. I Cᴀɴ Mᴇʀɢᴇ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs!, Aɴᴅ Uᴘʟᴏᴀᴅ Iᴛ Tᴏ Tᴇʟᴇɢʀᴀᴍ.

"""
