import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text_contains="Reklama", user_id=ADMINS)
async def send_ad_to_all_start(message: types.Message, state: FSMContext):
    await message.answer(f"Admin reklamangizni kiriting!")
    await state.set_state("reklama")

@dp.message_handler(state='reklama')
async def send_ad_to_all(message: types.Message, state: FSMContext):
    try:
        users = await db.select_all_users()
        for user in users:
            # print(user[3])
            user_id = user[3]
            await bot.send_message(chat_id=user_id, text=message.text)
            await asyncio.sleep(0.05)
    except:
        pass
    await state.finish()

@dp.message_handler(text_contains="Users", user_id=ADMINS)
async def send_to_users(message: types.Message):
    users = await db.select_all_users()
    users_len = len(users)
    users_arr = ""
    numbers = 0
    for user in users:
        numbers += 1
        users_arr += f"<b>{numbers}.</b>"
        users_arr += user[1]
        users_arr += "\n"
    users_arr += f"\n<b>Jami foydalanuvchilar: {users_len}</b>"
    await message.answer(text=users_arr)

