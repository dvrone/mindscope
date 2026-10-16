from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards.main_menu import main_menu

router = Router()


@router.callback_query(
    F.data.startswith("mbti:") | F.data.startswith("iq:") | F.data.startswith("eq:")
)
async def stale_button(callback: CallbackQuery):
    await callback.answer(
        "Bu test allaqachon tugagan yoki bekor qilingan. /start bosing.",
        show_alert=True,
    )


@router.message()
async def unknown_message(message: Message, state: FSMContext):
    if await state.get_state():
        await message.answer(
            "Test davom etmoqda. Javobni tugmalar orqali tanlang "
            "yoki /cancel bilan to'xtating."
        )
    else:
        await message.answer(
            "Tushunmadim. Menyudan test tanlang yoki /help yuboring.",
            reply_markup=main_menu(),
        )
