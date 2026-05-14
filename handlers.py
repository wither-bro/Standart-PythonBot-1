# / / ГЛАВНЫЙ ЗАПУСКНОЙ ФАЙЛ / /

import asyncio
import logging
from aiogram import Bot, Dispatcher
import config    # Импортируем наш секретный конфиг с токеном
import handlers  # Импортируем нашу логику и обработчики сообщений

# 1. Логирование — это "черный ящик" самолета. 
# Если бот упадет, здесь будет написано почему.
logging.basicConfig(level=logging.INFO)

# 2. Инициализация бота и диспетчера
# Мы берем токен прямо из нашего файла config.py
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

# 3. Подключаем наши обработчики (те самые кнопки и команды)
# Мы говорим диспетчеру: "Слушай то, что написано в handlers.py"
dp.include_router(handlers.router)

# 4. Функция запуска
async def main():
    print("--- БОТ ЗАПУЩЕН И ГОТОВ К РАБОТЕ ---")
    print("Напиши /start в своем Telegram-боте!")
    
    # Удаляем все сообщения, которые пришли боту, пока он был выключен
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Начинаем опрос серверов Telegram (Polling)
    await dp.start_polling(bot)

# Точка входа в программу
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен пользователем.")
