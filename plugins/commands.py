import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG
from utils import Media

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        await message.reply(INVITE_MSG)
    else:
        buttons = [[
            InlineKeyboardButton('🔎 sᴇᴀʀᴄʜ ʜᴇʀᴇ', switch_inline_query_current_chat=''),
            InlineKeyboardButton('📥 ɢᴏ ɪɴʟɪɴᴇ', switch_inline_query=''),
        ],[
        InlineKeyboardButton("📽 🄲🄸🄽🄴🄷🅄🄱 ", url="https://t.me/cinehub_family"),
        InlineKeyboardButton("📕 ᴀʙᴏᴜᴛ & ʜᴇʟᴘ", url="https://telegra.ph/ʜᴇʟᴘ-11-16"),
        ],[
        InlineKeyboardButton("🎞 සිංහල උපසිරැසි", url="https://t.me/sub_searcher_bot"),
        InlineKeyboardButton("🔀 🅢🅗🅐🅡🅔", url="https://telegram.me/share/url?url=https://t.me/media_searcher_bot"),
        ],[
        InlineKeyboardButton('🎬 ᴄʟɪᴄᴋ ᴛᴏ sᴇᴀʀᴄʜ мσνιє σя тν ѕєяιєѕ', switch_inline_query_current_chat=''),
    ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

 
@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type,
        'caption': reply.caption.html if reply.caption else None
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')


@Client.on_message(filters.command('help'))
async def go(bot, message):
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        await message.reply("<a href='https://telegra.ph/%CA%9C%E1%B4%87%CA%9F%E1%B4%98-11-16'>Tutorial Video of 🄲🄸🄽🄴🄷🅄🄱 ᴍᴇᴅɪᴀ sᴇᴀʀᴄʜᴇʀ ʙᴏᴛ</a> ", quote=True)
    else:
        buttons = [[
        InlineKeyboardButton("🏠 Mαιη Mєηυ ", callback_data='start'),
        InlineKeyboardButton("📚 ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ", url="https://telegra.ph/ʜᴇʟᴘ-11-16")
        ],[
        InlineKeyboardButton("🅢🅗🅐🅡🅔 & 🅢🅤🅟🅟🅞🅡🅣", url="https://telegram.me/share/url?url=https://t.me/media_searcher_bot"),
        ],[
        InlineKeyboardButton("🎬 ᴄʟɪᴄᴋ ᴛᴏ sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇ ᴏʀ ᴛᴠ sᴇʀɪᴇs", switch_inline_query_current_chat=''),
    ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply("📌 ѕтєρѕ\n\n1️⃣ ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ɴᴀᴍᴇᴅ <b>' 🎬 ᴄʟɪᴄᴋ ᴛᴏ sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇ ᴏʀ ᴛᴠ sᴇʀɪᴇs '</b>\n2️⃣ ᴛʜᴇɴ ᴛʏᴘᴇ ғɪʟᴍ ᴏʀ ᴛᴠ sᴇʀɪᴇs ɴᴀᴍᴇ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴛᴏ sᴇᴀʀᴄʜ \n3️⃣ sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ғɪʟᴇ (ᴀᴍᴏɴɢ ᴠᴀʀɪᴏᴜs ғᴏʀᴍᴀᴛs) & ᴅᴏᴡɴʟɪᴀᴅ ɪᴛ\n\n❔ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ʜᴇʟᴘ , ᴛᴀᴘ' 📕 ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ' ʙᴜᴛᴛᴏɴ ᴛᴏ ʀᴇsᴏʟᴠᴇ ʏᴏᴜ ɪssᴜᴇ\n\n🔅 𝐈𝐟 𝐭𝐡𝐞𝐫𝐞 𝐰𝐚𝐬𝐧'𝐭 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐦 𝐨𝐫 𝐓𝐕 𝐬𝐞𝐫𝐢𝐞𝐬 𝐉𝐮𝐬𝐭 𝐭𝐲𝐩𝐞 𝐚𝐬 𝐚 𝐧𝐨𝐫𝐦𝐚𝐥 𝐜𝐡𝐚𝐭 𝐰𝐞 𝐰𝐢𝐥𝐥 𝐮𝐩𝐥𝐨𝐚𝐝 𝐢𝐭 𝐚𝐬 𝐬𝐨𝐨𝐧 𝐚𝐬 𝐩𝐨𝐬𝐬𝐢𝐛𝐥𝐞\n\n<a href='https://t.me/media_searcher_bot'>🤖</a> | © ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ @cinehub_family ", reply_markup=reply_markup)

@Client.on_message(filters.command('info'))
async def info(bot, message):
    msg = await message.reply("😎 ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴍᴏᴠɪᴇs & ᴛᴠ sᴇʀɪᴇs sᴛᴏʀʏ ʟɪɴᴇ , ᴀᴄᴛᴏʀs , ʀᴇʟᴇsᴇ ᴅᴀᴛᴇ , .. .\n\n ᴡᴇ ʜᴀᴠᴇ ᴀʀʀᴀɴɢᴇ ɪᴛ ғᴏʀ ʏᴏᴜ ❕ \n\n🔥ᴊᴜsᴛ ᴘʀᴇss ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ sᴇᴀʀᴄʜɪɴɢ ᴍᴇᴅɪᴀ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴏᴠɪᴇ ᴏʀ ᴛᴠ sᴇʀɪᴇs ᴡʜᴀᴛ ᴇᴠᴇʀ ʏᴏᴜ ᴡᴀɴᴛ \n\nσρтιση ѕυρρσят ву : @imdb \n\n\n <b>😢 sorry still working on it</b>", quote=True)
