from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def mbti_answer_keyboard(question: dict) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"A) {question['a']['text']}", callback_data="mbti:a"
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"B) {question['b']['text']}", callback_data="mbti:b"
                )
            ],
        ]
    )
