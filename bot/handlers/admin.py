from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import ADMIN_ID
from bot.database import get_stats

router = Router()


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    # Faqat admin ko'ra oladi; boshqalarga bot jim turadi
    if message.from_user.id != ADMIN_ID:
        return

    users, total, per_test = await get_stats()

    lines = [
        "📈 <b>Statistika</b>\n",
        f"Foydalanuvchilar: <b>{users}</b>",
        f"Jami natijalar: <b>{total}</b>",
    ]
    for test_type, count in per_test:
        lines.append(f"{test_type}: {count}")

    await message.answer("\n".join(lines), parse_mode="HTML")
