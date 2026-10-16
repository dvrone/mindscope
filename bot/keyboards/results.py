from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def clear_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗑 Tarixni tozalash", callback_data="results:ask_clear"
                )
            ]
        ]
    )


def confirm_clear_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Ha, o'chirish", callback_data="results:clear"
                ),
                InlineKeyboardButton(text="❌ Yo'q", callback_data="results:cancel"),
            ]
        ]
    )
