import logging

from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_message(message: types.Message):
    await message.answer(
        text=f"Salom, {message.from_user.full_name}. Xush kelibsiz!"
    )

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

