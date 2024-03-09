import asyncio
import os
import time

from bot import (LOGGER, UPLOAD_AS_DOC, UPLOAD_TO_DRIVE, delete_all, formatDB,
                 gDict, queueDB)
from config import Config
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helpers.display_progress import Progress
from helpers.ffmpeg_helper import MergeSub, MergeVideo, take_screen_shot
from helpers.rclone_upload import rclone_driver, rclone_upload
from helpers.uploader import uploadVideo
from helpers.utils import UserSettings
from PIL import Image
from pyrogram import Client
from pyrogram.errors import MessageNotModified
from pyrogram.errors.rpc_error import UnknownError
from pyrogram.types import CallbackQuery

# Import statements...

async def download_media(c, media, user_id, n, all_count):
    try:
        c_time = time.time()
        prog = Progress(user_id, c, cb.message)
        file_dl_path = await c.download_media(
            message=media,
            file_name=f"downloads/{str(user_id)}/{str(media.id)}/vid.mkv",
            progress=prog.progress_for_pyrogram,
            progress_args=(f"🚀 Downloading: `{media.file_name}`", c_time, f"\n**Downloading: {n}/{all_count}**"),
        )
        return file_dl_path
    except UnknownError as e:
        LOGGER.info(e)
        return None
    except Exception as download_err:
        LOGGER.info(f"Failed to download Error: {download_err}")
        return None

async def merge_videos(c, cb, list_message_ids, list_subtitle_ids):
    # Existing code...
    # ...

    for n, i in enumerate(await c.get_messages(chat_id=cb.from_user.id, message_ids=list_message_ids)):
        media = i.video or i.document
        await cb.message.edit(f"📥 Starting Download of ... `{media.file_name}`")
        LOGGER.info(f"📥 Starting Download of ... {media.file_name}")
        await asyncio.sleep(5)
        
        file_dl_path = await download_media(c, media, cb.from_user.id, n + 1, all_count)
        
        if file_dl_path is None:
            continue

        # Rest of your code...

async def mergeNow(c: Client, cb: CallbackQuery, new_file_name: str):
    # Existing code...

    try:
        await merge_videos(c, cb, list_message_ids, list_subtitle_ids)
    except Exception as merge_err:
        LOGGER.error(f"Error during video merging: {merge_err}")
        await cb.message.edit("❌ Failed to merge video!")
        await cleanup_after_error(cb.from_user.id)
        return

    # Rest of your code...

    try:
        await upload_video(
            c, cb, merged_video_path, width, height, duration, video_thumbnail, os.path.getsize(merged_video_path), UPLOAD_AS_DOC[f"{cb.from_user.id}"]
        )
    except Exception as upload_err:
        LOGGER.error(f"Error during video upload: {upload_err}")
        await cb.message.edit("❌ Failed to upload video!")
        await cleanup_after_error(cb.from_user.id)
        return

async def cleanup_after_error(user_id):
    await delete_all(root=f"downloads/{str(user_id)}")
    queueDB.update({user_id: {"videos": [], "subtitles": [], "audios": []}})
    formatDB.update({user_id: None})
  
