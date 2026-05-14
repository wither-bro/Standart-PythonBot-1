# / / ГЛАВНЫЙ ЗАПУСКНОЙ ФАЙЛ / /

import asyncio
import logging
from aiogram import Bot, Dispatcher
import config    # Подключаем наш сейф с токеном
import handlers  # Подключаем наш мозг с хендлерами

# Настройка вывода информации в консоль
logging.basicConfig(level=logging.INFO)

async def main():
    # Инициализируем бота, забирая токен из config.py
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    # Сообщаем диспетчеру, что нужно использовать наши хендлеры
    dp.include_router(handlers.router)

    print("🚀 Бот от SERIES(CG) Studios успешно запущен!")
    
    # Пропускаем сообщения, которые пришли, пока бот спал
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запуск бесконечного цикла проверки сообщений
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен.")