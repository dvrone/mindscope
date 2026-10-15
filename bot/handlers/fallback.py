from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(
    F.data.startswith("mbti:") | F.data.startswith("iq:") | F.data.startswith("eq:")
)
async def stale_button(callback: CallbackQuery):
    await callback.answer(
        "Bu test allaqachon tugagan yoki bekor qilingan. /start bosing.",
        show_alert=True,
    )
