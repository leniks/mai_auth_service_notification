import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    CHAT_ID: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

settings = Settings()

def get_bot_creds():
    return {"TOKEN": settings.TELEGRAM_BOT_TOKEN,
            "ID": settings.CHAT_ID}