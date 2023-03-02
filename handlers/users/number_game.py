from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.states import Signup
from keyboards.inline.guess_btn import guess_inl_btn, guess_inl_btn_start, guess_inl_btn_stop
from loader import dp
import random

def guessnumber():
    number = random.randint(1,100)
    guess = 0
    print(number)
    while guess != number:
        guess = int(input("Son kiriting: "))
        if guess > number:
            print(f"{guess} dan kichik!")
        elif guess < number:
            print(f"{guess} dan katta!")
        else:
            print("Qoyil topdingiz!")

@dp.message_handler(text_contains='oyin')
async def guess_number(message: Message, state: FSMContext):
    text = f"<b>.:: Son-top Game ::.</b>\n\n<b>Men 1 dan 100 gacha son o'yladim toping?</b>"
    await message.answer(text=text, reply_markup=guess_inl_btn_start)
    await state.set_state('start')

@dp.message_handler(state='start')
async def guess_number_start(message: Message, state: FSMContext):
    text = f"<b>.:: Son-top Game ::.</b>\n\n" \
           f"<b>Men 1 dan 100 gacha son o'yladim toping?</b>" \
           f"\nIltimos son kiriting: ..."
    await message.answer(text=text, reply_markup=guess_inl_btn_stop)
    await state.set_state('update_game')




