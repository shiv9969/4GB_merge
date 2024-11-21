import os

class Config(object):
    API_HASH = os.environ.get("API_HASH", "cbabdb3f23de6326352ef3ac26338d9c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7609226318:AAEAnsDJFhqDDtnNYe_BYYuScYSrsqAy8UE")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "9301087")
    OWNER = os.environ.get("OWNER", "1525203313")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ASSAULTER_SHIV")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "BoB_Files1")
    PASSWORD = os.environ.get("PASSWORD", "Shiv")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Shivji:BoBfiles@cluster0.t1mka5v.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOG_CHANNEL", "-1002205049781")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCN7F8ALkT21kem46tpVh6HfitZbVmKugpZg6VUvPC_3TD2rk2xZ0VgMm8TM8hTIwIB47HQB5JiJBoiP-9hWeAJ5kTnGN0qpKFkikhpCOazW95gQekXnnaw8_7jMjJUuOoKM8RqrlO0LNQz6FNR52R6pE559P75P8Hn8G2qoivcM2mdpBfwqYBLpDXl3GLCWsJfgqIS6PX4wS_5pw3Eo7sKQweLh92a0QH__fMQnZjdQhe66JGgs8vh6w4yztWtuidB78WvNAnilGUc7q4T9HDVdWyCRFdQ4RPqh4QyJ1JurjfDIeMlSs9iYaXzNaZlv7mo1Joj0DsIGF2Ok8YDw74kZY8kfAAAAABa6MFxAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    UPSTREAM_REPO = "https://github.com/shiv9969/4GB_merge"
    UPSTREAM_BRANCH = "master"

    START_TEXT = """
Hɪ 👋 I Aᴍ A Fɪʟᴇ/Vɪᴅᴇᴏ Mᴇʀɢᴇ Bᴏᴛ. I Cᴀɴ Mᴇʀɢᴇ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs!, Aɴᴅ Uᴘʟᴏᴀᴅ Iᴛ Tᴏ Tᴇʟᴇɢʀᴀᴍ.

"""
