from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def eq_answer_keyboard(question: dict) -> InlineKeyboardMarkup:
    labels = ["A", "B", "C", "D"]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{labels[i]}) {option['text']}",
                    callback_data=f"eq:{i}",
                )
            ]
            for i, option in enumerate(question["options"])
        ]
    )
