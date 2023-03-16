from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

checkbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅', callback_data='yes'),
            InlineKeyboardButton(text='❌', callback_data='no')
        ]
    ]
)


async def answerbot(text, callbck):
    answer_btn = InlineKeyboardMarkup()
    check = InlineKeyboardButton(text=text, callback_data=callbck)
    answer_btn.insert(check)
    return answer_btn