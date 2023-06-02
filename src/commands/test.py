import subprocess
import typer

app = typer.Typer()

@app.command()
def test() -> None:
    subprocess.run(['pytest', '-v'])
