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
# GNU Affero General Pu
blic License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging 
import os

import subprocess

import logging

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Rest of the code...


from os import supports_dir_fd
from pyrogram import idle
from . import app, sudo_users

async def main():
    await app.start()
    print(f'[Started]: @{(await app.get_me()).username}')
    await idle()
    await app.stop()

COMMAND_HANDLERS = {

    '/start': start_command,

    '/help': help_command,

    '/encode': encode_command,

    '/mediainfo': mediainfo_command,

}

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

    bot.send_message(chat_id=chat_id, text=output.decode('utf-8'))
    
app.loop.run_until_complete(main())
