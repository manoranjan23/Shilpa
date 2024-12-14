import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_ID = "7080135405"
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7157587567))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/manoranjan23/Shilpa",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/somueditingzone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/somueditingzone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Strings_Gen_Robot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AMBOT = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AMOP = [
    "🚩ʜᴀʀ ʜᴀʀ ᴍᴀʜᴀᴅᴇᴠ 🚩\n🚩ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ🚩\n🚩ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {0}🍷\n\n๛ sᴏᴍᴜ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ᴛʜɪs ʙᴏᴛ ɪs ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ʟɪsᴛᴇɴ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ \n────────────────── \n➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ  ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\nʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ ๛ᴍʀsᴏᴍᴜ࿐"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/ppU.jpg"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://envs.sh/lkG.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/164d3363f4775c9a5e0e2.jpg"
STATS_VID_URL = "https://envs.sh/lkZ.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0e1c097742ea6ae5bc186.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/abf21ea063b2a5389a349.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/652198cfcbf20439646ac.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/77c52f7296918d486998c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/b0c6b818150b7b65355b4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/77c52f7296918d486998c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/7cacf7916705dd3649e92.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/7cc7183b82327933b7b04.jpg"
FAILED = "https://telegra.ph/file/7cacf7916705dd3649e92.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
