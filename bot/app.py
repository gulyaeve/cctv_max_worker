import logging

from maxapi import Bot
from bot.settings import settings

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.MAX_API_TOKEN)
