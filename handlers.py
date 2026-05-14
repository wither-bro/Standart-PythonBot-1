# / / ОБРАБОТЧИК СОБЫТИЙ / /
# Этот файл отвечает за то, ЧТО бот будет делать при нажатии на кнопки.

from aiogram import Router, F, types
from aiogram.filters import Command
import datetime  # Библиотека для работы со временем
import kb        # Импортируем наш файл с кнопками

# Роутер — это как распределитель задач. 
# Он понимает, какое сообщение к какому обработчику отправить.
router = Router()

# 1. Ответ на команду /start
@router.message(Command("start"))
async def start_handler(message: types.Message):
    # Мы отправляем текст и прикрепляем нашу клавиатуру из kb.py
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я готов к работе.",
        reply_markup=kb.main_menu()
    )

# 2. Обработка кнопки "Сколько время? ⏰"
@router.message(F.text == "Сколько время? ⏰")
async def time_handler(message: types.Message):
    # Получаем текущее время
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Сейчас на часах: {now} 🕒")

# 3. Обработка кнопки "Как тебя зовут? 🤔"
@router.message(F.text == "Как тебя зовут? 🤔")
async def name_handler(message: types.Message):
    await message.answer("Меня зовут Обучающий Бот! Я проект студии SERIES(CG).")

# 4. Обработка любого другого текста (Разговорный режим)
@router.message()
async def message_handler(message: types.Message):
    await message.answer("Я тебя услышал! Попробуй нажать на кнопки в меню.")

# ПОДСКАЗКА ДЛЯ НОВИЧКА:
# Если ты изменил текст кнопки в kb.py, не забудь изменить его и здесь
# в строчке F.text == "Твой новый текст", иначе бот не поймет нажатие!
