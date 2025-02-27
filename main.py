import os
from pathlib import Path
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import BotCommand, BotCommandScopeDefault, CallbackQuery, FSInputFile, Message

from config import load_bot_config

# Загружаем конфигурацию
config = load_bot_config()
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        "Привет!\n"
        "Я бот, который поможет тебе выгрузить информацию о документах с портала publication.pravo.gov.ru\n\n"
        "Доступные команды:\n"
        "🔹 /start - запуск бота и просмотр этого сообщения\n"
        "🔹 /help - получить справку о работе бота\n"
        "🔹 /get_documents - начать выбор дат для получения документов\n\n"
        "Для начала работы выберите одну из команд выше или воспользуйтесь меню команд."
    )


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        "Справка по работе с ботом:\n\n"
        "1️⃣ Для получения документов используйте команду /get_documents\n"
        "2️⃣ После этого откроется календарь для выбора начальной даты\n"
        "3️⃣ Выберите начальную дату и затем конечную дату\n"
        "4️⃣ Бот обработает ваш запрос и пришлет документ с результатами\n\n"
        "Если вам нужно начать сначала, просто отправьте /start\n"
        "Для повторного просмотра этой справки используйте /help"
    )


# Создаем список команд для меню
async def set_commands():
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Получить справку"),
        BotCommand(command="get_documents", description="Выбрать даты и получить документы"),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


# Добавляем инициализацию команд при запуске бота
async def start_bot():
    await set_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(start_bot())