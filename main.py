import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.config import BOT_TOKEN
from bot.database import init_db
from bot.handlers import eq, fallback, iq, mbti, results, start

logging.basicConfig(level=logging.INFO)


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Asosiy menyu"),
            BotCommand(command="cancel", description="Testni to'xtatish"),
            BotCommand(command="help", description="Yordam"),
        ]
    )


async def main():
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(mbti.router)
    dp.include_router(iq.router)
    dp.include_router(eq.router)
    dp.include_router(results.router)
    dp.include_router(fallback.router)

    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
