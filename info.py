import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = '👋 Hey There !\n\n <b>ɪ ᴀᴍ  🄲🄸🄽🄴🄷🅄🄱 ᴍᴇᴅɪᴀ sᴇᴀʀᴄʜᴇʀ ʙᴏᴛ ɪɴ ᴄɪɴᴇʜᴜʙ ᴄᴏᴍᴍᴜɴɪᴛʏ . . .</b>\nමට පුලුවන් ඔයාට ඕන කර ғɪʟᴍ එක ᴛᴠ sᴇʀɪᴇs එක හොයල දෙන්න . . .\n
ඔයාලට මොකක් හරි ගැටලුවක් ආවොත් ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ එක හරි message එකක් හරි දාන්න\n😇 ආ ! අපේ ᴅᴀᴛᴀʙᴀsᴇ එකේ ඔයා හොයන ғɪʟᴍ ᴏʀ ᴛᴠ sᴇʀɪᴇs තිබ්බෙ නැත්නම් message එකක් දාලා තියන්න අපි පුලුවන් ඉක්මනට ᴜᴘʟᴏᴀᴅ කරන්නම්\n\n⚡️ <b>ʙᴏᴛ ɴᴀᴍᴇ : @media_searcher_bot</b>\n\n🍀 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ; @cinehub_family\n\n💠 ᴊᴜsᴛ ᴘʀᴇss sᴇᴀʀᴄʜ ʙᴜᴛᴛᴏɴs ᴀɴᴅ sᴛᴀʀᴛ sᴇᴀʀᴄʜɪɴɢ ᴏʀ ʏᴏᴜ ᴄᴀɴ sᴇᴀʀᴄʜ ғɪʟᴇs ɪɴ ɪɴʟɪɴᴇ ᴍᴏᴅᴇ ᴜsɪɴɢ ᴍᴇ\n\n🅢🅗🅐🅡🅔 & 🅢🅤🅟🅟🅞🅡🅣 🔗https://t.me/media_searcher_bot'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
