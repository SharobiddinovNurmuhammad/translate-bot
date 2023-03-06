import asyncio
import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from keyboards.default.startmenu import admin_menustart
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(CommandStart(), user_id=ADMINS[0])
async def bot_start_admin(message: types.Message):
    await message.answer("Xush kelibsiz admin!", reply_markup=admin_menustart)

@dp.message_handler(text="👥Foydalanuvchilar󠁧󠁢", user_id=ADMINS[0])
async def count_name_users(message: types.Message):
    users = db.select_all_users()
    text = "<code>Botdagi jami foydalanuvchilar:\n\n"
    count = 0
    for user in users:
        count += 1
        text += f"{count}. "
        text += f"{user[1]}\n"
    text += f"\nJami: {count} ta</code>"
    await bot.send_message(chat_id=ADMINS[0], text=text)

@dp.message_handler(text="📰Reklama", user_id=ADMINS[0])
async def reklama(message: types.Message, state: FSMContext):
    await message.answer("Xabaringizni kiriting: ")
    await state.set_state('rek')

@dp.message_handler(state='rek')
async def send_reklama(message: types.Message, state: FSMContext):
    msg = message.text
    users = db.select_all_users()
    for user in users:
        user = user[0]
        await bot.send_message(chat_id=user, text=msg)
        time.sleep(0.05)
    await message.answer("Xabar yetkazildi")
    await state.finish()



