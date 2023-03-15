# VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging 
import os 
import subprocess



import subprocess

import logging

from telegram.ext import CommandHandler, MessageHandler, Updater

# Rest of the code...


from os import supports_dir_fd
from pyrogram import idle
from . import app, sudo_users

async def main():
    await app.start()
    print(f'[Started]: @{(await app.get_me()).username}')
    await idle()
    await app.stop()

def start_command(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello, welcome to the Video Encoder Bot!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/encode - encode/compress a video\n'
                              '/mediainfo - get technical information about a video')


def encode_command(update, context):
    """Compress a video using h264 codec."""
    chat_id = update.message.chat_id

    # Check if a video file was sent with the command
    if not update.message.video:
        context.bot.send_message(chat_id=chat_id, text='Please send a video file with the /encode command.')
        return

    # Get the file ID of the video file
    file_id = update.message.video.file_id

    # Download the video file
    video_file = context.bot.get_file(file_id)

    # Encode the video using h264 codec and save it as a file
    new_file_path = f'{file_id}.mp4'
    subprocess.run(['ffmpeg', '-i', video_file.download_as_bytearray(), '-c:v', 'libx264', new_file_path])

    # Send the compressed video file back to the user
    with open(new_file_path, 'rb') as f:
        context.bot.send_video(chat_id=chat_id, video=f)

    # Delete the compressed video file from the server
    os.remove(new_file_path)


def mediainfo_command(bot, update):
    chat_id = update.message.chat_id

    # Check if a video file was sent with the command
    if not update.message.video:
        bot.send_message(chat_id=chat_id, text='Please send a video file with the /mediainfo command.')
        return

    # Get the file ID of the video file
    file_id = update.message.video.file_id

    # Download the video file
    video_file = bot.get_file(file_id)

    # Run the mediainfo command on the video file
    output = subprocess.check_output(['mediainfo', '--Output=JSON', video_file.download_as_bytearray()])

    # Send the technical information back to the user
    bot.send_message(chat_id=chat_id, text




    




