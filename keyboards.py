from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Клавиатура внизу чата

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

#Клавиатура под сообщением

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Музыка", callback_data='music')],
   [InlineKeyboardButton(text="Видео", callback_data='video')]
])

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://www.rbc.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/')],
   [InlineKeyboardButton(text="Видео", url='https://rutube.ru/')]
])
#Третий способ создания клавиатуры — билдер
test = ["Опция 1", "Опция 2"]

async def test_keyboard():
      keyboard = InlineKeyboardBuilder()
      for key in test:
         keyboard.add(KeyboardButton(text=key))
      return keyboard.adjust(2).as_markup()

# inline клавиатура
async def dyn_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()