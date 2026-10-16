from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "MindScope botiga xush kelibsiz!\n\n" "Quyidagi testlardan birini tanlang:",
        reply_markup=main_menu(),
    )


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Test bekor qilindi. Quyidagi testlardan birini tanlang:",
        reply_markup=main_menu(),
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "<b>MindScope</b> shaxsiyatingiz, IQ va EQ darajangizni taxminan aniqlaydi.\n\n"
        "🧠 MBTI testi: 4 harfli shaxsiyat tipingizni aniqlaydi\n"
        "📊 IQ testi: mantiqiy fikrlash bo'yicha taxminiy IQ ball\n"
        "❤️ EQ testi: emotsional intellektni to'rt soha bo'yicha baholaydi\n"
        "📋 Mening natijalarim: oxirgi natijalaringiz\n\n"
        "Buyruqlar:\n"
        "/start: asosiy menyu\n"
        "/cancel: testni to'xtatish\n"
        "/help: shu yordam xabari",
        parse_mode="HTML",
    )
