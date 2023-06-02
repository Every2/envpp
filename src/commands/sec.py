import typer
from typing_extensions import Annotated
from typing import List
import subprocess

app = typer.Typer()

@app.command()
def sec(files: Annotated[List[str], typer.Argument(help="Passe um arquivo ou os arquivos, por exemplo: foo.py, too.py")]):
    subprocess.run(['pip-audit'])
    for file in files:
        subprocess.run(['bandit', file])
