from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram import F, Router
import app.keyboards as kb
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
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
    await callback.message.answer(reply_markup=await kb.view_questions)
    await callback.answer()
