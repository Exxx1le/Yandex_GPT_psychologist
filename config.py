from dataclasses import dataclass
from typing import Type

from environs import Env


@dataclass
class ConfigItem:
    """Base class for configuration items."""

    pass


@dataclass
class TgBot(ConfigItem):
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class YandexAssistant(ConfigItem):
    folder_id: str  # папка доступа к cloud Yandex


@dataclass
class BotConfig:
    tg_bot: TgBot


@dataclass
class YandexConfig:
    folder_config: YandexAssistant


def load_config(config_class: Type[ConfigItem], env_key: str, path: str | None = None) -> ConfigItem:
    """
    Loads a configuration object from environment variables.

    Args:
        config_class: The class of the configuration object to create (e.g., TgBot, YandexAssistant).
        env_key: The name of the environment variable to retrieve the value from.
        path: Optional path to the .env file.

    Returns:
        An instance of the specified configuration class with values loaded from the environment.
    """
    env = Env()
    env.read_env(path)
    if config_class == TgBot:
        return config_class(token=env(env_key))
    elif config_class == YandexAssistant:
        return config_class(folder_id=env(env_key))
    else:
        raise ValueError(f"Unsupported config class: {config_class}")


def load_bot_config(path: str | None = None) -> BotConfig:
    """Loads the Telegram Bot configuration."""
    tg_bot = load_config(TgBot, "BOT_TOKEN", path)
    return BotConfig(tg_bot=tg_bot)


def load_yandex_config(path: str | None = None) -> YandexConfig:
    """Loads the Yandex Assistant configuration."""
    yandex_assistant = load_config(YandexAssistant, "YANDEX_FOLDER", path)
    return YandexConfig(folder_config=yandex_assistant)
