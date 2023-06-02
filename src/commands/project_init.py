import typer
from typing_extensions import Annotated
from libs.lib import AppError
import subprocess
import os

app = typer.Typer()

@app.command()
def project_init(
    project_name: Annotated[str, typer.Argument(help="Nome do seu projeto")],
    docs: Annotated[bool, typer.Option(help = "Cria um diretório para documentação, por exemplo: something.md")] = False,
    scripts: Annotated[bool, typer.Option(help = "Cria um diretório para scripts, por exemplo: something.sh")] = False,
    tests: Annotated[bool,  typer.Option(help= "Cria um diretório para testes usando pytest")] = True
):
    try:
        path = os.path.join(os.getcwd(), project_name)
        os.makedirs(path)
        os.chdir(project_name)
        subprocess.run(['pdm', 'init'])
        subprocess.run(['pdm', 'add', 'mypy', 'pytest', 'pip-audit', 'bandit'])
    except:
        AppError("Diretório já existe")
    
    if tests:
        files = ['__init__.py', 'test.py']
        path = os.path.join(os.getcwd(), 'tests')
        os.makedirs(path)
        for file in files:
            with open(f"tests/{file}", "w") as f:
                f.write("")

    if docs:
           path = os.path.join(os.getcwd(), 'docs')
           os.makedirs(path)
           with open("docs/start.md", "w") as file:
               file.write(f"")
       
    if scripts:
        path = os.path.join(os.getcwd(), 'scripts')
        os.makedirs(path)
        with open("scripts/start.sh", "w") as file:
            file.write("")
