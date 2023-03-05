from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startmenu import menustart, admin_menustart
from data.config import ADMINS
from loader import dp, db

@dp.message_handler(CommandStart(), user_id=ADMINS[0])
async def bot_start_admin(message: types.Message):
    await message.answer("Xush kelibsiz admin!", reply_markup=admin_menustart)

@dp.message_handler(text='👥Foydalanuvchilar󠁧󠁢', user_id=ADMINS[0])
async def bot_users(message: types.Message):
    users = await db.select_all_users()
    count_user = 0
    text = "<b>Botdagi foydalanuvchilar:</b>\n"
    for user in users:
        count_user += 1
        text += user[1]
        text += '\n'
    text += f'\nJami: {count_user} ta'
    await message.answer(text=text)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menustart)
    try:
        await db.add_user(message.from_user.full_name, message.from_user.id)
        await message.bot.send_message(chat_id=ADMINS[0],
                                       text=f"{message.from_user.full_name} botga qo'shildi!"
                                       )
    except:
        pass

@dp.message_handler(text='📊Statistika')
async def get_statistika(message: types.Message):
    count = await db.count_users()
    await message.answer(f"{count}")


