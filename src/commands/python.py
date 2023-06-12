import typer
from typing_extensions import Annotated
from libs.lib import AppError
import subprocess
import os
from typing import List

app = typer.Typer()

@app.command()
def init(
    project_name: Annotated[str, typer.Argument(help="Nome do seu projeto")],
    docs: Annotated[bool, typer.Option(help = "Cria um diretório para documentação, por exemplo: something.md")] = False,
    scripts: Annotated[bool, typer.Option(help = "Cria um diretório para scripts, por exemplo: something.sh")] = False,
    tests: Annotated[bool,  typer.Option(help= "Cria um diretório para testes usando pytest")] = True,
    docker: Annotated[bool, typer.Option(help='Cria um dockerfile simples')] = False
) -> None:
    
    try:
        subprocess.run(['pdm', 'init'])
        subprocess.run(['pdm', 'add', 'mypy', 'pytest', 'pip-audit', 'bandit'])
    except:
        AppError('Você não tem o pdm instalado, instalando....')
        subprocess.run(['pip', 'install', '--user', 'pdm'])
        path = os.path.join(os.getcwd(), project_name)
        os.makedirs(path)
        os.chdir(project_name)
        subprocess.run(['pdm', 'init'])
        subprocess.run(['pdm', 'add', 'mypy', 'pip-audit', 'bandit'])
    
    if tests:
        subprocess.run(['pdm', 'add', 'pytest'])
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
               file.write("")
       
    if scripts:
        path = os.path.join(os.getcwd(), 'scripts')
        os.makedirs(path)
        with open("scripts/start.sh", "w") as file:
            file.write("")

    if docker:
        with open('Dockerfile', 'w') as file:
            file.write('FROM python:3.11-buster\n\nRUN mkdir app\n\nWORKDIR /app\n\n')

@app.command()
def lint() -> None:
    subprocess.run(['mypy', '--strict', '.'])

@app.command()
def sec(files: Annotated[List[str], typer.Argument(help="Passe um arquivo ou os arquivos, por exemplo: foo.py, too.py")]) -> None:
    subprocess.run(['pip-audit'])
    for file in files:
        subprocess.run(['bandit', file])    

@app.command()
def test() -> None:
    subprocess.run(['pytest', '-v'])
