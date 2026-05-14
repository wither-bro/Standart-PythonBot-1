# / / ТВОЙ КОНСТРУКТОР КНОПОК / /

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Здесь мы создаем функцию, которую вызовем в основном коде.
# Она соберет все кнопки в красивое меню.
def main_menu():
    # Мы используем Builder — это как конструктор LEGO для кнопок.
    builder = ReplyKeyboardBuilder()
    
    # Добавляем кнопки. 
    builder.add(KeyboardButton(text="Сколько время? ⏰"))
    builder.add(KeyboardButton(text="Как тебя зовут? 🤔"))
    builder.add(KeyboardButton(text="Расскажи анекдот 🤡"))
    builder.add(KeyboardButton(text="Связь с создателем 👨‍💻"))
    
    # А вот и наша новая кнопка для поднятия настроения!
    builder.add(KeyboardButton(text="Подбодри меня! 🌟"))
    
    # Мы указали 2, значит кнопки будут идти парами, а последняя растянется.
    builder.adjust(2)
    
    # resize_keyboard=True делает кнопки аккуратными, а не на пол-экрана.
    return builder.as_markup(resize_keyboard=True)

# ПОДСКАЗКА ДЛЯ НОВИЧКА:
# Видишь, как просто? Добавил одну строчку builder.add — и у бота новая функция!
# Попробуй поменять текст в кавычках на свой, например: "Мой секрет 🤫"
