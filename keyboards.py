from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Клавиатура внизу чата
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Клавиатура под сообщением для задания 2
inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://www.rbc.ru/')],
    [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/')],
    [InlineKeyboardButton(text="Видео", url='https://rutube.ru/')]
])

# Клавиатура под сообщением для задания 3
inline_keyboard_more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

# Третий способ создания клавиатуры — билдер
test = ["Опция 1", "Опция 2"]

# Inline клавиатура
async def dyn_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=key.lower()))  # Добавляем callback_data
    return keyboard.adjust(1).as_markup()
