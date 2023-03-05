import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="📰Reklama", user_id=ADMINS[0])
async def send_ad_to_all(message: types.Message, state: FSMContext):
    await message.answer("Xabaringizni kirting:")
    await state.set_state('admin_rek')

@dp.message_handler(state='admin_rek')
async def send_ad_to_all(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    msg = message.text
    for user in users:
        # print(user[3])
        user_id = user[1]
        await bot.send_message(chat_id=user_id, text=msg)
        await asyncio.sleep(0.05)
    await message.answer("Xabar yetkazildi!")
    await state.finish()