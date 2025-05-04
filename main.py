import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random

from gtts import gTTS
import os

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

import keyboards as kb

@dp.message(CommandStart())
async def start(message: Message):
# Вызов клавиатуры внизу
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)
# Вызов inline клавиатуры
#   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)
# Вызов билдера
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=await kb.test_keyboard())

@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f' Привет, {message.from_user.first_name}',reply_markup=kb.main)

@ dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f' Пока, {message.from_user.first_name}')

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())