import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/users", user_id=ADMINS)
async def send_to_users(message: types.Message):
    users = await db.select_all_users()
    users_arr = ""
    for user in users:
        users_arr += user[1]
        users_arr += "\n"
    await message.answer(text=users_arr)

