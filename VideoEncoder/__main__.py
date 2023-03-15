import logging
from os import supports_dir_fd
from pyrogram import idle
from . import app, sudo_users

async def main():
    await app.start()
    print(f'[Started]: @{(await app.get_me()).username}')
    await idle()
    await app.stop()

app.loop.run_until_complete(main())







    




