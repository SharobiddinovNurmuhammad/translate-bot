from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admins_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="♻Reklama")
        ],
        [
            KeyboardButton(text="👥Users")
        ],
    ]
)