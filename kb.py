# / / ТВОЙ КОНСТРУКТОР КНОПОК / /

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Здесь мы создаем функцию, которую вызовем в основном коде.
# Она соберет все кнопки в красивое меню.
def main_menu():
    # Мы используем Builder — это как конструктор LEGO для кнопок.
    builder = ReplyKeyboardBuilder()
    
    # Добавляем кнопки. Текст внутри — это то, что бот получит от пользователя.
    builder.add(KeyboardButton(text="Сколько время? ⏰"))
    builder.add(KeyboardButton(text="Как тебя зовут? 🤔"))
    builder.add(KeyboardButton(text="Расскажи анекдот 🤡"))
    builder.add(KeyboardButton(text="Связь с создателем 👨‍💻"))
    
    # Здесь мы указываем, сколько кнопок будет в одном ряду.
    # Число 2 означает, что кнопки будут идти парами.
    builder.adjust(2)
    
    # as_markup превращает наш конструктор в готовую клавиатуру.
    # resize_keyboard=True делает кнопки аккуратными и маленькими.
    return builder.as_markup(resize_keyboard=True)

# ПОДСКАЗКА ДЛЯ НОВИЧКА:
# Хочешь добавить свою кнопку? Просто скопируй строчку 
# builder.add(KeyboardButton(text="Твой текст")) и вставь ниже!
