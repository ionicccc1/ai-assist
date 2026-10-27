import click
from .commands import status, ask, config


@click.group()
def cli():
    """
    AiCLI - утилита для запросов к ИИ прямо из терминала
    """
    pass

cli.add_command(status)
cli.add_command(ask)
cli.add_command(config)

if __name__ == "__main__":
    cli()