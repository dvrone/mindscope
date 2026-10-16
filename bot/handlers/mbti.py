from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.data.mbti_questions import MBTI_QUESTIONS
from bot.data.mbti_types import MBTI_TYPES
from bot.database import save_result
from bot.keyboards.mbti import mbti_answer_keyboard
from bot.states import MBTITest


def calculate_type(scores: dict) -> str:
    result = ""
    for first, second in ("EI", "SN", "TF", "JP"):
        # Ball teng bo'lsa, birinchi harf olinadi
        if scores.get(first, 0) >= scores.get(second, 0):
            result += first
        else:
            result += second
    return result


router = Router()


@router.message(F.text == "🧠 MBTI testi")
async def start_mbti(message: Message, state: FSMContext):
    await state.set_state(MBTITest.answering)
    await state.update_data(index=0, scores={})

    question = MBTI_QUESTIONS[0]
    await message.answer(
        f"1/{len(MBTI_QUESTIONS)}\n\n{question['text']}",
        reply_markup=mbti_answer_keyboard(question),
    )


@router.callback_query(MBTITest.answering, F.data.in_({"mbti:a", "mbti:b"}))
async def handle_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    scores = data["scores"]

    question = MBTI_QUESTIONS[index]
    choice = "a" if callback.data == "mbti:a" else "b"
    letter = question[choice]["letter"]
    scores[letter] = scores.get(letter, 0) + 1

    index += 1
    await state.update_data(index=index, scores=scores)

    if index < len(MBTI_QUESTIONS):
        next_question = MBTI_QUESTIONS[index]
        await callback.message.edit_text(
            f"{index + 1}/{len(MBTI_QUESTIONS)}\n\n{next_question['text']}",
            reply_markup=mbti_answer_keyboard(next_question),
        )
    else:
        mbti_type = calculate_type(scores)
        info = MBTI_TYPES[mbti_type]
        await save_result(callback.from_user.id, "MBTI", mbti_type)
        await state.clear()
        await callback.message.edit_text(
            f"✅ Test tugadi!\n\n"
            f"Sizning MBTI tipingiz: <b>{mbti_type}</b> — {info['name']}\n\n"
            f"{info['description']}",
            parse_mode="HTML",
        )

    await callback.answer()
