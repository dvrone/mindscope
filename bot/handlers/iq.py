from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.data.iq_questions import IQ_QUESTIONS
from bot.keyboards.iq import iq_answer_keyboard
from bot.states import IQTest


def calculate_iq(correct: int, total: int) -> int:
    # Oddiy chiziqli shkala: 0% -> 70, 100% -> 145
    return round(70 + (correct / total) * 75)


def iq_level(iq: int) -> str:
    if iq >= 130:
        return "Juda yuqori"
    if iq >= 115:
        return "Yuqori"
    if iq >= 85:
        return "O'rtacha"
    return "O'rtachadan past"


router = Router()


@router.message(F.text == "📊 IQ testi")
async def start_iq(message: Message, state: FSMContext):
    await state.set_state(IQTest.answering)
    await state.update_data(index=0, correct=0)

    question = IQ_QUESTIONS[0]
    await message.answer(
        f"1/{len(IQ_QUESTIONS)}\n\n{question['text']}",
        reply_markup=iq_answer_keyboard(question),
    )


@router.callback_query(IQTest.answering, F.data.startswith("iq:"))
async def handle_iq_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    correct = data["correct"]

    chosen = int(callback.data.split(":")[1])
    if chosen == IQ_QUESTIONS[index]["correct"]:
        correct += 1

    index += 1
    await state.update_data(index=index, correct=correct)

    if index < len(IQ_QUESTIONS):
        next_question = IQ_QUESTIONS[index]
        await callback.message.edit_text(
            f"{index + 1}/{len(IQ_QUESTIONS)}\n\n{next_question['text']}",
            reply_markup=iq_answer_keyboard(next_question),
        )
    else:
        total = len(IQ_QUESTIONS)
        iq = calculate_iq(correct, total)
        level = iq_level(iq)
        await state.clear()
        await callback.message.edit_text(
            f"✅ Test tugadi!\n\n"
            f"To'g'ri javoblar: {correct}/{total}\n"
            f"Taxminiy IQ: <b>{iq}</b>\n"
            f"Daraja: {level}\n\n"
            "⚠️ Bu rasmiy IQ testi emas, faqat o'yin-kulgi va taxminiy baho uchun.",
            parse_mode="HTML",
        )

    await callback.answer()
