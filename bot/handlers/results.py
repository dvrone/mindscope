from aiogram import F, Router
from aiogram.types import Message

from bot.database import get_results

router = Router()


@router.message(F.text == "📋 Mening natijalarim")
async def show_results(message: Message):
    rows = await get_results(message.from_user.id)

    if not rows:
        await message.answer(
            "Sizda hali saqlangan natijalar yo'q. Avval biror testni yeching."
        )
        return

    lines = ["📋 <b>Oxirgi natijalaringiz:</b>\n"]
    for test_type, result, created_at in rows:
        date = created_at[:16]
        lines.append(f"{date} | {test_type}: <b>{result}</b>")

    await message.answer("\n".join(lines), parse_mode="HTML")
