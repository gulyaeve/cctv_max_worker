from urllib.parse import quote

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MAX_API_TOKEN: str
    MAX_CHAT_ID: str

    # RabbitMQ
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str

    @property
    def rabbitmq_url(self) -> str:
        return (
            f"amqp://{self.RABBITMQ_DEFAULT_USER}:{quote(self.RABBITMQ_DEFAULT_PASS)}@" f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"
        )
    
    QUEUE_NAME: str = "cctv_max"
    EXCHANGE_NAME: str = "cctv_msg_send"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Объект с переменными окружения
settings = Settings()

