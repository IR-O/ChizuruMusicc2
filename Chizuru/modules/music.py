import os, aiofiles, aiohttp, ffmpeg, random, re, requests
from typing import Callable
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.errors import UserAlreadyParticipant
from youtube_search import YoutubeSearch

from Chizuru import Chizuru, pytgcalls, userbot
from Chizuru.core.admin_func import authorized_users
from Chizuru.core import utils as rq
from Chizuru.core.utils import DurationLimitError, get_audio_stream, get_video_stream
from Chizuru.core.thumb_func import generate_cover

from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import AudioQuality
from pytgcalls.types.input_stream.parameters import AudioParameters
from pytgcalls.types import Update


DURATION_LIMIT = 300

keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data="close_data")]]
)

local_thumb = [
    "https://graph.org/file/e3fa9ab16ebefbfdd29d9.jpg",
    "https://graph.org/file/5938774f48c1f019c73f7.jpg",
    "https://graph.org/file/b13a16734bab174f58482.jpg",
    "https://graph.org/file/2deb4e5cbba862f2d5457.jpg",
]

# ============================= PLAY AUDIO ============================= #

@Chizuru.on_message(filters.command(["play"], prefixes=["/", "."]))
async def play(_, message: Message):
    chat_id = message.chat.id
    user_name = message.from_user.mention
    msg = await message.reply("🔎 sᴇᴀʀᴄʜɪɴɢ...")

    if len(message.command) < 2:
        return await msg.edit("💌 ᴜsᴀɢᴇ: /play song name")

    query = message.text.split(None, 1)[1]

    results = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{results[0]['url_suffix']}"
    title = results[0]["title"][:40]
    duration = results[0]["duration"]
    views = results[0]["views"]
    thumbnail = results[0]["thumbnails"][0]

    await generate_cover(user_name, title, views, duration, thumbnail)

    file_path = await get_audio_stream(link)

    if chat_id in pytgcalls.active_calls:
        position = await rq.put(chat_id, file=file_path)

        await message.reply_photo(
            photo="final.png",
            caption=f"➻ ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ » {position}\n\n🏷️ {title}",
            reply_markup=keyboard,
        )
    else:
        await pytgcalls.play(
            chat_id,
            AudioPiped(
                file_path,
                AudioParameters.from_quality(AudioQuality.STUDIO),
            ),
        )

        await message.reply_photo(
            photo="final.png",
            caption=f"▶️ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ\n🏷️ {title}",
            reply_markup=keyboard,
        )

    os.remove("final.png")
    await msg.delete()


# ============================= PLAY VIDEO ============================= #

@Chizuru.on_message(filters.command(["vplay"], prefixes=["/", "."]))
async def vplay(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("💌 ᴜsᴀɢᴇ: /vplay video name")

    query = message.text.split(None, 1)[1]
    results = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{results[0]['url_suffix']}"

    file_path = await get_video_stream(link)

    if chat_id in pytgcalls.active_calls:
        position = await rq.put(chat_id, file=file_path)
        return await message.reply(f"Queued at {position}")

    await pytgcalls.play(chat_id, AudioVideoPiped(file_path))
    await message.reply("▶️ ᴠɪᴅᴇᴏ sᴛʀᴇᴀᴍɪɴɢ sᴛᴀʀᴛᴇᴅ")


# ============================= SKIP ============================= #

@Chizuru.on_message(filters.command(["skip", "next"], prefixes=["/", "!"]))
async def skip(_, message: Message):
    chat_id = message.chat.id

    if chat_id not in pytgcalls.active_calls:
        return await message.reply("❌ ɴᴏᴛʜɪɴɢ ᴘʟᴀʏɪɴɢ")

    rq.task_done(chat_id)

    if rq.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
        return await message.reply("⏹ Queue ended")

    await pytgcalls.play(chat_id, AudioPiped(rq.get(chat_id)["file"]))
    await message.reply("⏭ sᴋɪᴘᴘᴇᴅ")


# ============================= STREAM END ============================= #

@pytgcalls.on_stream_end()
async def on_stream_end(_, update: Update):
    chat_id = update.chat_id
    rq.task_done(chat_id)

    if rq.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
        return

    await pytgcalls.play(chat_id, AudioPiped(rq.get(chat_id)["file"]))


# ============================= PAUSE / RESUME ============================= #

@Chizuru.on_message(filters.command("pause"))
async def pause(_, msg: Message):
    await pytgcalls.pause_stream(msg.chat.id)
    await msg.reply("⏸ paused")


@Chizuru.on_message(filters.command("resume"))
async def resume(_, msg: Message):
    await pytgcalls.resume_stream(msg.chat.id)
    await msg.reply("▶️ resumed")


# ============================= STOP ============================= #

@Chizuru.on_message(filters.command(["end", "leavevc"]))
async def stop(_, msg: Message):
    await pytgcalls.leave_group_call(msg.chat.id)
    await msg.reply("⏹ stopped")


# ============================= VOLUME ============================= #

@Chizuru.on_message(filters.command("volume"))
async def volume(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /volume 1-200")

    vol = int(message.command[1])
    await pytgcalls.change_volume_call(message.chat.id, vol)
    await message.reply(f"🔊 volume set to {vol}%")
