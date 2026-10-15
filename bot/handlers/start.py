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
