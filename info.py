import re
from os import environ,getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SESSION = environ.get('SESSION', 'Media_search')
LOG_STR = "Current Cusomized Configurations are:-\n"
PORT = environ.get("PORT", "8080")
PICS = (environ.get('PICS', 'https://graph.org/file/e06884276bd3509a53789.jpg https://graph.org/file/b067051e3174a10d594dc.jpg https://graph.org/file/05533805967ce71b56ffd.jpg https://graph.org/file/076933e2890a49660cce2.jpg https://graph.org/file/4d2514ed8fe32a7c96e08.jpg https://graph.org/file/16bc6fddd93b4d7edf4a9.jpg https://graph.org/file/5fe4190f87099c28d0131.jpg https://graph.org/file/7b784b9f5f45f73983e6c.jpg https://graph.org/file/9b2e9d2efe57ab516fdf7.jpg https://graph.org/file/63cb1e6397c9ae5dafa18.jpg https://graph.org/file/2bd3bed47ae39163d593c.jpg https://graph.org/file/cbbb19d8db5cfe3a74a9f.jpg https://graph.org/file/4e4d3947cf48da07bbf00.jpg https://graph.org/file/4c768c2f4678b4eb991b8.jpg https://graph.org/file/fa4b19f5fe1a9f1ffce93.jpg https://graph.org/file/b311448e4638b103d9001.jpg https://graph.org/file/62579dd48a40cef899d2c.jpg https://graph.org/file/0c62f3a6ce5d511553b3f.jpg https://graph.org/file/d7cd6ba2b18819379b4a7.jpg https://graph.org/file/4976dc115338cddd99c38.jpg https://graph.org/file/f575a2c98328346e18269.jpg https://graph.org/file/830d4d71d92a882c1e838.jpg https://graph.org/file/cd36a4949e278d0692de2.jpg https://graph.org/file/bfa019019302879ec44c0.jpg https://graph.org/file/a0e6f952add3ad336c3e1.jpg https://graph.org/file/bfe6f373f9be4df3174b8.jpg https://graph.org/file/34de67d70e95582415ddc.jpg https://graph.org/file/803eb18697788d538aa7d.jpg https://graph.org/file/ed8814513f8fd5c5668c1.jpg https://graph.org/file/55d5bc0856d2cc8198553.jpg https://graph.org/file/2020172acb3e20b904fa4.jpg https://graph.org/file/ba0540b18a6350e4437b4.jpg https://graph.org/file/a2e7e286741620c45b71f.jpg https://graph.org/file/5a8176401dafeb33f8c1f.jpg https://graph.org/file/484aaa6042f8f6eb7bbfe.jpg https://graph.org/file/195d814b564d31ab85086.jpg https://graph.org/file/7cadab25fa7862a12816a.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/a56a9c555e43529b2d2f9.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/64afb8fff79e1b3d1706Fa'))
CODE = (environ.get('CODE', 'https://graph.org/file/64afb8fff79e1b3d17066.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'cuty.io'))
STREAM_API = (environ.get('STREAM_API', 'b544b38b14b065b405ad7873cd783165c9a998fb'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/HowToOpenLinkHP/69'))

PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '10')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1week')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/64afb8fff79e1b3d17066.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 30ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜs\n- 120ʀs - 3 ᴍᴏɴᴛʜs\n- 220ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\n✨ ᴜᴘɪ ɪᴅ - <code>jivshn@okaxis</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')
OWNER_USERNAME = environ.get('OWNER_USERNAME', '') # owner username without @
# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
syd_channel = environ.get('SYD_CHANNEL', '')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
SYD_CHANNEL = int(syd_channel) if syd_channel and id_pattern.search(syd_channel) else None
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel
