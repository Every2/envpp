import subprocess
import typer

app = typer.Typer()

@app.command()
def lint() -> None:
    subprocess.run(['mypy', '--strict', '.'])
