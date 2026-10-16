import random

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.data.eq_questions import EQ_QUESTIONS
from bot.database import save_result
from bot.keyboards.eq import eq_answer_keyboard
from bot.states import EQTest

AREA_NAMES = {
    "self_awareness": "O'zini anglash",
    "self_regulation": "O'zini boshqarish",
    "empathy": "Empatiya",
    "social": "Ijtimoiy ko'nikmalar",
}

# Har savol uchun maksimal ball 4, sohalar soni 4
MAX_TOTAL = len(EQ_QUESTIONS) * 4
MAX_PER_AREA = MAX_TOTAL // len(AREA_NAMES)


def eq_level(total: int) -> str:
    # Daraja umumiy maksimal ballning ulushiga qarab aniqlanadi
    ratio = total / MAX_TOTAL
    if ratio >= 0.83:
        return "Juda yuqori"
    if ratio >= 0.67:
        return "Yuqori"
    if ratio >= 0.5:
        return "O'rtacha"
    return "Rivojlantirish kerak"


def build_area_report(scores: dict) -> str:
    lines = []
    for area, name in AREA_NAMES.items():
        value = scores.get(area, 0)
        filled = round(value / MAX_PER_AREA * 5)
        bar = "🟩" * filled + "⬜" * (5 - filled)
        lines.append(f"{name}: {bar} {value}/{MAX_PER_AREA}")
    return "\n".join(lines)


router = Router()


@router.message(F.text == "❤️ EQ testi")
async def start_eq(message: Message, state: FSMContext):
    # Savollar tartibi har testda tasodifiy
    order = random.sample(range(len(EQ_QUESTIONS)), len(EQ_QUESTIONS))

    await state.set_state(EQTest.answering)
    await state.update_data(index=0, scores={}, order=order)

    question = EQ_QUESTIONS[order[0]]
    await message.answer(
        f"1/{len(EQ_QUESTIONS)}\n\n{question['text']}",
        reply_markup=eq_answer_keyboard(question),
    )


@router.callback_query(EQTest.answering, F.data.startswith("eq:"))
async def handle_eq_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    scores = data["scores"]
    order = data["order"]

    question = EQ_QUESTIONS[order[index]]
    chosen = int(callback.data.split(":")[1])
    score = question["options"][chosen]["score"]

    area = question["area"]
    scores[area] = scores.get(area, 0) + score

    index += 1
    await state.update_data(index=index, scores=scores)

    if index < len(EQ_QUESTIONS):
        next_question = EQ_QUESTIONS[order[index]]
        await callback.message.edit_text(
            f"{index + 1}/{len(EQ_QUESTIONS)}\n\n{next_question['text']}",
            reply_markup=eq_answer_keyboard(next_question),
        )
    else:
        total = sum(scores.values())
        level = eq_level(total)
        report = build_area_report(scores)
        await save_result(callback.from_user.id, "EQ", f"{total}/{MAX_TOTAL}")
        await state.clear()
        await callback.message.edit_text(
            f"✅ Test tugadi!\n\n"
            f"Umumiy ball: <b>{total}/{MAX_TOTAL}</b>\n"
            f"Daraja: {level}\n\n"
            f"{report}\n\n"
            "⚠️ Bu rasmiy test emas, faqat o'z-o'zini bilish uchun taxminiy baho.",
            parse_mode="HTML",
        )

    await callback.answer()
