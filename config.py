import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в .env или в окружении.")

# Если переменная не задана, админ-функции будут недоступны.
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")  # может быть None

# Пути к файлам данных
DATA_DIR = Path(__file__).parent / "data"
REG_FILE = DATA_DIR / "registrations.json"
HEROES_FILE = DATA_DIR / "heroes.json"

# Настройки прокси (опционально)
PROXY_TYPE = os.getenv("PROXY_TYPE")
PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")
PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")