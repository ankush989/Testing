from configs import Config
from database.db import db
from pyrogram import Client
from pyrogram.types import Message

async def add_user_to_db(Client, Message):
    if not await db.is_user_exist(Message.from_user.id):
        await db.add_user(Message.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await Client.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{Message.from_user.first_name}](tg://user?id={Message.from_user.id}) started @FluxTrialBot !!"
            )
