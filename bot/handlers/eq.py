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

MAX_TOTAL = 48
MAX_PER_AREA = 12


def eq_level(total: int) -> str:
    # Minimal ball 12, maksimal 48
    if total >= 40:
        return "Juda yuqori"
    if total >= 32:
        return "Yuqori"
    if total >= 24:
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
    await state.set_state(EQTest.answering)
    await state.update_data(index=0, scores={})

    question = EQ_QUESTIONS[0]
    await message.answer(
        f"1/{len(EQ_QUESTIONS)}\n\n{question['text']}",
        reply_markup=eq_answer_keyboard(question),
    )


@router.callback_query(EQTest.answering, F.data.startswith("eq:"))
async def handle_eq_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    scores = data["scores"]

    question = EQ_QUESTIONS[index]
    chosen = int(callback.data.split(":")[1])
    score = question["options"][chosen]["score"]

    area = question["area"]
    scores[area] = scores.get(area, 0) + score

    index += 1
    await state.update_data(index=index, scores=scores)

    if index < len(EQ_QUESTIONS):
        next_question = EQ_QUESTIONS[index]
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
