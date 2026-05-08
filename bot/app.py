import logging

from maxapi import Bot
from maxapi.enums.parse_mode import ParseMode
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types.attachments.buttons.callback_button import CallbackButton

from bot.settings import settings

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.MAX_API_TOKEN, parse_mode=ParseMode.HTML)


def build_incident_answer_keyboard(incident_id: int, text: str ="Ответить на инцидент") -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.row(
        CallbackButton(text=text, payload=f"INC_ANS_{incident_id}"),
    )
    return kb