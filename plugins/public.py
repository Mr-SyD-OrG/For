import re
import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from database import db
from config import Config

API_ID = Config.API_ID
API_HASH = Config.API_HASH
ADMINS = Config.OWNER_ID
DATABASE_NAME = Config.DB_NAME
MONGO_URL = Config.DB_URL


@Client.on_message(filters.private & filters.command(["fwd", "forward"]))
async def run(bot, message):
    try:
        user_id = message.from_user.id
        text = await bot.send_message(
            user_id,
            "<b><u>Set Bot</u></b>\n\nForward A Message From Bot Father ᴄᴀɴᴛɪᴀɴɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ... \n/cancel - To Cancel This Process"
        )

        try:
            bots_ids = await bot.listen(chat_id=user_id, timeout=300)
        except asyncio.exceptions.TimeoutError:
            return await text.edit_text('Process Has Been Automatically Cancelled')

        if bots_ids.text == "/cancel":
            await bots_ids.delete()
            return await text.edit_text("Process Canceled")
        elif not bots_ids.forward_date or (bots_ids.forward_from and bots_ids.forward_from.id != 93372553):
            await bots_ids.delete()
            return await text.edit_text("This Is Not A Forward Message From The Correct User")
        
        msg = await message.reply_text("**👨‍💻 ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ❣️**")

        bot_id_match = re.findall(r'\d{8,10}', message.text)
        bot_id = int(bot_id_match[0]) if bot_id_match else None

        bot_token_match = re.findall(r'\d{8,10}:[0-9A-Za-z_-]{35}', bots_ids.text, re.IGNORECASE)
        bot_token = bot_token_match[0] if bot_token_match else None

        user_nam_match = re.findall(r'@[A-Za-z_-]+bot', message.text, re.IGNORECASE)
        username = user_nam_match[0].lstrip('@') if user_nam_match else None

        try:
            ai = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "MrSyD"},
            )
            await ai.start()
            bot_info = await ai.get_me()

            details = {
                'user_id': user_id,
                'bot_id': bot_id,
                'token': bot_token,
                'name': username,
                'username': username
            }
            await db.add_bot(user_id=user_id, bot_id=bot_id, bot_token=bot_token, username=username)
            await bots_ids.delete()
            await msg.edit_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴏɴᴇᴅ ʏᴏᴜʀ ʙᴏᴛ: @{bot_info.username}.")
        except Exception as e:
            logging.exception("Error while cloning bot.")
            await msg.edit_text(f"⚠️ <b>Bot Error:</b>\n\n<code>{e}</code>\n\n**Kindly forward this message to @SyD_XyZ to get assistance.**")
    except asyncio.exceptions.TimeoutError:
        await text.edit_text('Process Has Been Automatically Cancelled')

