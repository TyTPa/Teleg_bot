import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random
from gtts import gTTS
import os
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    # Вызов клавиатуры внизу
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)
    # Вызов inline клавиатуры
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)
    # Вызов билдера
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=await kb.test_keyboard())

# Обработка клавиатуры с reply кнопками
@dp.message(F.text == "Привет")
async def test_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}')

# Вызов inline клавиатуры
@dp.message(Command(commands=['link']))
async def link_command(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)

# Обработка клавиатуры с inline кнопками и билдером
@dp.message(Command(commands=['dynamic']))
async def dynamic_command(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_more)

@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer("Подгружаем", show_alert=True)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.dyn_keyboard())

@dp.callback_query(F.data == 'опция 1')
async def option_1(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали Опцию 1, {callback.from_user.first_name}')

@dp.callback_query(F.data == 'опция 2')
async def option_2(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали Опцию 2, {callback.from_user.first_name}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
