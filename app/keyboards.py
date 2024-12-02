from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, InlineKeyboardBuilder)

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Информация о боте', callback_data='info_bot'),
            InlineKeyboardButton(
            text='Перейти на сайт', url='https://moscowzoo.ru/')
         ], [InlineKeyboardButton(
            text='Перейти ТГ канал', url='https://t.me/Moscowzoo_official')
            ], [InlineKeyboardButton(
                text='Пройти викторину "Моё тотемное животное"',
                callback_data='quiz')
                ],
            ])

questions = ['1 вопрос', '2 вопрос', '3 вопрос']


async def view_questions():
    keyboard = InlineKeyboardBuilder()
    for question in questions:
        keyboard.add(InlineKeyboardButton(text=question, url='https://moscowzoo.ru/animals/kinds'))
    return keyboard.adjust(2).as_markup()
