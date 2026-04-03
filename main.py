import asyncio
import logging
import aio_pika
from faststream import FastStream
from bot.schemas import IncidentFullInfo
from bot.settings import settings
from bot.app import bot
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
    if incident.cameras_screenshots:
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
            text=str(incident)
        )


async def main():
    # async with broker:
    #     max_queue: aio_pika.RobustQueue = await broker.declare_queue(queue)
    #     max_exchange: aio_pika.RobustExchange = await broker.declare_exchange(exchange)
    #     await max_queue.bind(exchange=max_exchange)
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
