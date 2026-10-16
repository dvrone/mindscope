import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()
logger = logging.getLogger(__name__)


@router.errors()
async def on_error(event: ErrorEvent):
    logger.error("Kutilmagan xatolik: %s", event.exception, exc_info=event.exception)

    text = "Xatolik yuz berdi. Iltimos, /start bosib qayta urinib ko'ring."
    update = event.update

    try:
        if update.message:
            await update.message.answer(text)
        elif update.callback_query:
            await update.callback_query.answer(text, show_alert=True)
    except Exception:
        # Xabar yuborib bo'lmasa ham bot to'xtab qolmasligi kerak
        pass

    return True
