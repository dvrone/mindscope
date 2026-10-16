import asyncio
import logging
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.config import BOT_TOKEN
from bot.database import init_db
from bot.handlers import admin, eq, errors, fallback, iq, mbti, results, start


def setup_logging():
    handlers = [
        logging.StreamHandler(),
        RotatingFileHandler(
            "bot.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"
        ),
    ]
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=handlers,
    )


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Asosiy menyu"),
            BotCommand(command="cancel", description="Testni to'xtatish"),
            BotCommand(command="help", description="Yordam"),
        ]
    )


async def main():
    setup_logging()
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(mbti.router)
    dp.include_router(iq.router)
    dp.include_router(eq.router)
    dp.include_router(results.router)
    dp.include_router(admin.router)
    dp.include_router(fallback.router)
    dp.include_router(errors.router)

    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
