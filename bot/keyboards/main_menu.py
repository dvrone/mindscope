from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧠 MBTI testi")],
            [KeyboardButton(text="📊 IQ testi"), KeyboardButton(text="❤️ EQ testi")],
        ],
        resize_keyboard=True,
    )
