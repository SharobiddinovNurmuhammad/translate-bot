from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menustart = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='♻Tarjimon bot󠁧󠁢'),
            KeyboardButton(text='💬Fikr bildirish')
        ],
        [
            KeyboardButton(text='📊Statistika')
        ]
    ]
)

admin_menustart = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='♻Tarjimon bot󠁧󠁢'),
            KeyboardButton(text='💬Fikr bildirish')
        ],
        [
            KeyboardButton(text='👥Foydalanuvchilar󠁧󠁢'),
            KeyboardButton(text='📰Reklama')
        ],
        [
            KeyboardButton(text='📊Statistika')
        ]
    ]
)

