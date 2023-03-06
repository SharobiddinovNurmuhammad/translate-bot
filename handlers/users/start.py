import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startmenu import menustart
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menustart)
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name)
    except sqlite3.IntegrityError as err:
        pass
    user = db.select_user(id=message.from_user.id)
    await bot.send_message(chat_id=ADMINS[0],text=f"{user[1]} qo'shildi bazaga")

@dp.message_handler(text='📊Statistika')
async def get_statistika(message: types.Message):
    count = db.count_users()
    await message.answer(f"👥 Botdagi obunachilar:  {count[0]} ta\n\n"
                         f"📊  @etarjimonrobot statistikasi")


