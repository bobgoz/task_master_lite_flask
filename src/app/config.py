"""Параметры приложения."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
ENV_PATH = BASE_DIR / '.env'

is_env = load_dotenv(ENV_PATH)
if not is_env:
    raise RuntimeError(
        f'Файл {ENV_PATH} не найден, пуст или не содержит переменных.',
    )


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG', True) == 'true'


config = Config()
