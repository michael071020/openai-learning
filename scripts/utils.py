# scripts/utils.py
import os
from dotenv import load_dotenv

load_dotenv()  # 讀取本地 .env

def get_env(name: str, default=None):
    val = os.getenv(name, default)
    if val is None:
        raise EnvironmentError(f"Environment variable {name} not set. Please set it in .env")
    return val

# 常用設定
OPENAI_API_KEY = get_env("OPENAI_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "256"))
