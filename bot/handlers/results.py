from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from bot.database import clear_results, get_results
from bot.keyboards.results import clear_keyboard, confirm_clear_keyboard

router = Router()

TZ = ZoneInfo("Asia/Tashkent")


def format_date(value: str) -> str:
    # Bazada vaqt UTC'da saqlanadi, ko'rsatishda Toshkent vaqtiga o'tkazamiz
    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    return dt.astimezone(TZ).strftime("%d.%m.%Y %H:%M")


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
        lines.append(f"{format_date(created_at)} | {test_type}: <b>{result}</b>")

    await message.answer(
        "\n".join(lines),
        parse_mode="HTML",
        reply_markup=clear_keyboard(),
    )


@router.callback_query(F.data == "results:ask_clear")
async def ask_clear(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=confirm_clear_keyboard())
    await callback.answer("Rostdan ham barcha natijalar o'chirilsinmi?")


@router.callback_query(F.data == "results:clear")
async def do_clear(callback: CallbackQuery):
    await clear_results(callback.from_user.id)
    await callback.message.edit_text("🗑 Barcha natijalaringiz o'chirildi.")
    await callback.answer()


@router.callback_query(F.data == "results:cancel")
async def cancel_clear(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=confirm_clear_keyboard())
    await callback.answer("Bekor qilindi.")
