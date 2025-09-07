import click


@click.command()
@click.argument("prompt")
def cli(prompt: str) -> None:
    """A simple CLI that echoes the provided prompt."""
    click.echo(f"Prompt received: {prompt}")


if __name__ == "__main__":
    cli()