from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def iq_answer_keyboard(question: dict) -> InlineKeyboardMarkup:
    labels = ["A", "B", "C", "D"]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{labels[i]}) {option}",
                    callback_data=f"iq:{i}",
                )
            ]
            for i, option in enumerate(question["options"])
        ]
    )
