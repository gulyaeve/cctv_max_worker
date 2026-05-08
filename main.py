import asyncio
import logging
from faststream import FastStream
from bot.schemas import IncidentFullInfo
from bot.settings import settings
from bot.app import bot, build_incident_answer_keyboard
from faststream.rabbit import RabbitBroker, RabbitQueue, ExchangeType, RabbitExchange
from maxapi.types import InputMedia


# Настройка логирования
logging.basicConfig(level=logging.INFO)


queue = RabbitQueue(settings.QUEUE_NAME, auto_delete=False)
exchange = RabbitExchange(settings.EXCHANGE_NAME, ExchangeType.FANOUT)
broker = RabbitBroker(url=settings.rabbitmq_url)
app = FastStream(broker)


@broker.subscriber(queue, exchange)
async def incident_max_handler(incident: IncidentFullInfo):
    logging.info(incident)
    screenshot_dir = "/screenshots"
    # if incident.status == 0:
    #     text = "Оставить отзыв"
    # else:
    #     text = "Ответить на инцидент"
    
    if incident.cameras_screenshots:
        # photos = [
        #     build_incident_answer_keyboard(
        #         incident_id=incident.id,
        #         text=text
        #     ).as_markup()
        # ]
        photos = []
        for screenshot in incident.cameras_screenshots:
            photos.append(
                InputMedia(
                    f"{screenshot_dir}/{screenshot}"
                )
            )
        logging.info(photos)
        await bot.send_message(
            chat_id=settings.MAX_CHAT_ID,
            attachments=photos,
            text=str(incident)
        )
    else:
        await bot.send_message(
            chat_id=settings.MAX_CHAT_ID,
            text=str(incident),
            # attachments=[
            #     build_incident_answer_keyboard(
            #         incident_id=incident.id,
            #         text=text
            #     ).as_markup()
            # ]
        )


async def main():
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
