import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
env_path = root_dir / ".env"

load_dotenv(dotenv_path=env_path)

AI_TOKEN = os.getenv("AI_TOKEN")
api_url = os.getenv("api_url")
AI_PROMPT = "Ты - CLI-утилита. Твоя задача отвечать на вопросы пользователя без лишней информации. Ты помнишь только 1 запрос, поэтому уложись в 1 не длинный ответ. Без любой разметки(Markdown, HTML и т.п.)"
ai_client = OpenAI(
    base_url=api_url,
    api_key=AI_TOKEN
)