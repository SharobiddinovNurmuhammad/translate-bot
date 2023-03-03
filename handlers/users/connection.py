from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.default.startmenu import menustart
from keyboards.inline.connectkeyboard import checkbtn
from keyboards.inline.connectkeyboard import answerbot
from data.config import ADMINS
from loader import dp

@dp.message_handler(text_contains='Fikr bildirish')
async def question(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.full_name}, xabaringizni kiriting.', reply_markup=ReplyKeyboardRemove(True))
    await state.set_state('connect')

@dp.message_handler(state='connect')
async def questioncheck(message: Message, state: FSMContext):
    text = message.text
    name = message.from_user.full_name
    await state.update_data(chat_id=message.from_user.id, name=name, text=message.text)
    await message.answer(f"{text}\n\n<b>Xabarni jo'nataymi?</b>", reply_markup=checkbtn)
    await state.set_state('connectcheck')

@dp.callback_query_handler(state='connectcheck')
async def questionmsg(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    chat_id = user_data.get('chat_id')
    name = user_data.get('name')
    text = user_data.get('text')
    if call.data == 'yes':
        await call.bot.send_message(chat_id=ADMINS[0], text=f"<b>{name}</b>dan xabar keldi!\n\n{text}", reply_markup=await answerbot('Javob yozish',chat_id))
        await call.message.answer(text='✅Xabar yetkazildi', reply_markup=menustart)
        await call.message.delete()
        await state.finish()
    elif call.data == 'no':
        await call.message.answer(text='❌Xabar yetkazilmadi', reply_markup=menustart)
        await call.message.delete()
        await state.finish()

#Admindan javob uchun

@dp.callback_query_handler()
async def answerbutton(call: CallbackQuery, state: FSMContext):
    admin = call.message.reply_markup['inline_keyboard'][0][0]['text']
    if admin == 'Javob yozish':
        await state.update_data(chat_id=call.data)
        await call.message.edit_text(text=call.message.text, reply_markup=await answerbot('✅Javob berdingiz', 'admin'))
        await call.message.answer(f"Nurmuhammad, javobingizni kiriting:")
        await state.set_state('answermsg')

@dp.message_handler(state='answermsg')
async def answercheck(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(f"{text}\n\n<b>Xabarni jo'nataymi?</b>", reply_markup=checkbtn)
    await state.set_state('answertekshir')

@dp.callback_query_handler(state='answertekshir')
async def answermessage(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    chat_id = user_data.get('chat_id')
    text = user_data.get('text')
    if call.data == 'yes':
        await call.bot.send_message(chat_id=chat_id, text=f"<b>Admindan xabar:</b>\n\n{text}")
        await call.message.answer(text='✅Xabar yetkazildi', reply_markup=menustart)
        await call.message.delete()
        await state.finish()
    elif call.data == 'no':
        await call.message.answer(text='❌Xabar yetkazilmadi', reply_markup=menustart)
        await call.message.delete()
        await state.finish()