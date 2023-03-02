from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

guess_inl_btn = InlineKeyboardMarkup(row_width=3)

guess_inl_btn_start = InlineKeyboardMarkup(row_width=1)
start_game = InlineKeyboardButton(text="Start game", callback_data='boshlash')
guess_inl_btn_start.add(start_game)

guess_inl_btn_stop = InlineKeyboardMarkup(row_width=1)
stop_game = InlineKeyboardButton(text="Stop game", callback_data='toxta')
guess_inl_btn_stop.add(stop_game)