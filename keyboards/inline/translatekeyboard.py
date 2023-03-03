from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menutranslate = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿Inglizcha', callback_data='en'),
            InlineKeyboardButton(text='🇷🇺Ruscha', callback_data='ru')
        ],
        [
            InlineKeyboardButton(text="🇺🇿O'zbekcha", callback_data='uz')
        ],
        [
            InlineKeyboardButton(text='🔙Menyuga qaytish', callback_data='back')
        ]
    ]
)