import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.admin_btn import admins_btn
from loader import dp, db, bot
from data.config import ADMINS
@dp.message_handler(CommandStart(), user_id=ADMINS[0])
async def bot_start_admin(message: types.Message):
    text=f"👋Admin botga xush kelibsiz!"
    await message.answer(text, reply_markup=admins_btn)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer("Xush kelibsiz!")

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)


