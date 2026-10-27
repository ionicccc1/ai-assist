import click
from pathlib import Path
from Ai.config import AI_PROMPT, ai_client
from rich.console import Console


console = Console()

@click.command()
def status():
    """Проверка статуса утилиты"""
    click.echo("Начинаю проверку...")

    root_dir = Path(__file__).resolve().parent.parent.parent
    env_path = root_dir / ".env"

    if env_path.exists():
        click.secho("Файл конфигурации найден", fg="green")
    else:
        click.secho("Ошибка: файл .env отсутствует в корне проекта", fg="red", err=True)

@click.command()
@click.argument('prompt')
@click.option(
    '-m', '--model',
    default='google/gemini-2.5-flash-lite',
    help='Модель ИИ для отправки запроса'
)
def ask(prompt: str, model: str):
    """Запрос к ИИ"""
    with console.status("[bold green]Отправка запроса...", spinner="dots"):
        response = ai_client.chat.completions.create(
            model=model,
            max_tokens=2048,
            messages=[
                {"role": "system", "content": AI_PROMPT},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            text_piece = chunk.choices[0].delta.content
            click.echo(text_piece, nl=False)

    click.echo()


@click.command()
@click.option(
    '--key',
    prompt='Введите ваш API ключ',
    hide_input=True,
    help='API-ключ для авторизации запроса'
)
@click.option(
    '--max-tokens',
    type=click.IntRange(1, 8192),
    default=2048,
    help='Максимальное кол-во токенов в ответе(от 1 до 8192)'
)
def config(key: str, max_tokens: int):
    """Настроить параметры и API-ключ"""
    # masked_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
    # Функция добавления
    click.secho("Конфигурация успешно принята", fg="green")