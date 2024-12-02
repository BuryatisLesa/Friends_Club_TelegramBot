from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
# from aiogram.filters.callback_data import CallbackData
from aiogram import F, Router
import app.keyboards as kb
import sqlite3
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    connection = sqlite3.connect('friendsclub.sql')
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS animals(
                animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(500) NOT NULL,
                image_url VARCHAR(255)
                )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descriptions VARCHAR(1000) NOT NULL,
                animal_id INTEGER,
                FOREIGN KEY(animal_id) REFERENCES animals(animal_id))''')
    await message.reply(f'Привет. '
                        f'{message.from_user.first_name}',
                        reply_markup=kb.main)


@router.callback_query(F.data == 'info_bot')
async def view_info(callback: CallbackQuery):
    bot_description = (
        "ZooBuddy — бот для участия в программе \"Возьми животное под опеку\".\n\n"
        "Эта инициатива помогает заботиться о животных в Московском зоопарке. ",
        "Благодаря пожертвованиям можно поддерживать содержание более 6 000 обитателей зоопарка. "
        "Опека доступна для многих животных, от сурикатов до слонов.\n\n",
        "Став опекуном, вы сможете следить за своим подопечным и участвовать в улучшении его условий. "
        "Программа подходит как для частных лиц, так и для организаций. "
        "Поддержите биоразнообразие и помогите зоопарку вместе с ZooBuddy!"
    )
    for text in bot_description:
        await callback.message.answer(text=text)
    await callback.answer()


@router.callback_query(F.data == 'quiz')
async def start_quiz(callback: CallbackQuery):
    question = (
        'Как вы любите проводить время?'
    )
    await callback.message.edit_text(text=question,
                                     reply_markup=await kb.view_questions())
    await callback.answer()
