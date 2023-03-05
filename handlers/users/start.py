import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startmenu import menustart, admin_menustart
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(CommandStart(), user_id=ADMINS[0])
async def bot_start_admin(message: types.Message):
    await message.answer("Xush kelibsiz admin!", reply_markup=admin_menustart)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menustart)
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
@dp.message_handler(text='👥Foydalanuvchilar󠁧󠁢', user_id=ADMINS[0])
async def bot_users(message: types.Message):
    users = db.select_all_users()
    count_user = 0
    text = "<b>Botdagi foydalanuvchilar:</b>\n"
    for user in users:
        count_user += 1
        text += user[0][0]
        text += '\n'
    text += f'\nJami: {count_user} ta'
    await message.answer(text=text)

@dp.message_handler(text='📊Statistika')
async def get_statistika(message: types.Message):
    count = db.count_users()
    await message.answer(f"{count[0]}")


