
import re
import asyncio 
from .utils import STS
from database import db
from config import temp 
from translation import Translation
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait 
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate as PrivateChat
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified, ChannelPrivate
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
 


 
#===================Run Function===================#

@Client.on_message(filters.private & filters.command(["fwd", "forward"]))
async def run(bot, message):
    try:
        user_id = message.from_user.id
        text = await bot.send_message(user_id, "<b><u>Set Target Chat</u></b>\n\nForward A Message From Your Target Chat\n/cancel - To Cancel This Process")
        bots_ids = await bot.listen(chat_id=user_id, timeout=300)
        if bots_ids.text=="/cancel":
           await bots_ids.delete()
           return await text.edit_text(
                 "Process Canceled",
                 reply_markup=InlineKeyboardMarkup(buttons))
        elif not bots_ids.forward_date:
           await bots_ids.delete()
           return await text.edit_text("This Is Not A Forward Message")
        else:
           user_id = user_id
           bot_id = re.findall(r'\d[0-9]{8,10}', message.text)
           bot_id = int(bot_id[0]) if bot_id else None
           bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', bots_ids.text, re.IGNORECASE)
           bot_token = bot_token[0] if bot_token else None
           user_nam = re.findall(r'@[A-Za-z_-]+bot', message.text, re.IGNORECASE)
           username = user_nam[0].lstrip('@') if user_nam else None
         bots = await db.add_bot(user_id=user_id, bot_id=bot_id, bot_token=bot_token, username=username)
         await bots_ids.delete()
         await text.edit_text(
            "Successfully Updated" if bot else "This Channel Already Added",
            reply_markup=InlineKeyboardMarkup(buttons))
    except asyncio.exceptions.TimeoutError:
         await text.edit_text('Process Has Been Automatically Cancelled', reply_markup=InlineKeyboardMarkup(buttons))
  
