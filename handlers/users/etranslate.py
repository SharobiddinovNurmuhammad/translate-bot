from googletrans import Translator
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.default.startmenu import menustart
from keyboards.inline.translatekeyboard import menutranslate
from loader import dp

tarjimon = Translator()

@dp.message_handler(text_contains='Tarjimon')
async def tarjimonbot(message: Message, state: FSMContext):
    await message.answer(text="Tarjima qilish uchun matn yoki so'z kiriting: ", reply_markup=ReplyKeyboardRemove(True))
    await state.set_state('tarjimon')

@dp.message_handler(state='tarjimon')
async def tarjimonmenu(message: Message, state: FSMContext):
    await message.answer(text=message.text, reply_markup=menutranslate)

@dp.callback_query_handler(state='tarjimon')
async def etarjimaqil(call: CallbackQuery, state: FSMContext):
    text = call.message.text
    til = tarjimon.detect(text).lang
    if call.data == 'back':
        await call.answer(cache_time=1)
        await call.message.delete()
        await call.message.answer('Menyu:', reply_markup=menustart)
        await state.finish()
    elif call.data == 'en':
            if til != 'en':
                await call.message.edit_text(text=tarjimon.translate(text, dest='en').text, reply_markup=menutranslate)
            elif til == 'en':
                await call.answer(text="❌Matn o'zi Ingliz tilida, iltimos boshqa tilni tanlang", show_alert=True)
    elif call.data == 'ru':
            if til != 'ru':
                await call.message.edit_text(text=tarjimon.translate(text, dest='ru').text, reply_markup=menutranslate)
                await call.answer(cache_time=1)
            elif til == 'ru':
                await call.answer(text="❌Matn o'zi Rus tilida, iltimos boshqa tilni tanlang", show_alert=True)
                await call.answer(cache_time=1)
    elif call.data == 'uz':
        if til != 'uz':
            await call.message.edit_text(text=tarjimon.translate(text, dest='uz').text, reply_markup=menutranslate)
            await call.answer(cache_time=1)
        elif til == 'uz':
            await call.answer(text="❌Matn o'zi O'zbek tilida, iltimos boshqa tilni tanlang", show_alert=True)
            await call.answer(cache_time=1)






