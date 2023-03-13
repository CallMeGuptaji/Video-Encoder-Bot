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
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters

from .. import data
from ..utils.tasks import handle_task
from ..utils.utils import check_user

video_mimetype = [
    "video/x-flv",
    "video/mp4",
    "application/x-mpegURL",
    "video/MP2T",
    "video/3gpp",
    "video/quicktime",
    "video/x-msvideo",
    "video/x-ms-wmv",
    "video/x-matroska",
    "video/webm",
    "video/x-m4v",
    "video/quicktime",
    "video/mpeg"
]

import os
import ffmpeg

def encode_video(input_file, output_file):
    # Get the video duration
    probe = ffmpeg.probe(input_file)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    duration = float(video_stream['duration'])

    # Set the encoding options
    input_video = ffmpeg.input(input_file)
    output_video = input_video.output(output_file, codec='libx264', crf=23, preset='medium', tune='film', vf=f"scale=-2:360")
    output_video.run()

    # Get the size of the encoded file
    size = os.path.getsize(output_file)

    # Return the duration and size of the encoded video
    return duration, size


