import logging

from maxapi import Bot
from maxapi.enums.parse_mode import ParseMode
from bot.settings import settings

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.MAX_API_TOKEN, parse_mode=ParseMode.HTML)
