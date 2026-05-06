import logging

from maxapi import Bot
from maxapi.enums.parse_mode import ParseMode
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types.attachments.buttons.callback_button import CallbackButton

from bot.settings import settings

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.MAX_API_TOKEN, parse_mode=ParseMode.HTML)


def build_main_keyboard() -> InlineKeyboardBuilder:
    kb = InlineKeyboardBuilder()
    kb.row(
        CallbackButton(text="Ответить на инцидент DEMO", payload="INC_ANS"),
    )
    return kb