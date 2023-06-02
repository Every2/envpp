import typer
from typing_extensions import Annotated
import os
import sys
import subprocess

app = typer.Typer()

@app.command()
def init(
    project_name: Annotated[str, typer.Argument(help='Nome do seu projeto')],
    vcpkg: Annotated[bool, typer.Option(help="Instala o vcpkg para gerenciamento de libs(Obs: Precisa do git instalado)")] = False,
    tests: Annotated[bool,  typer.Option(help= "Cria um diretório para testes")] = True,
    build: Annotated[bool,  typer.Option(help= "Cria um diretório para build")] = False,
) -> None:
    directories = ['src', 'include', 'lib', 'bin']
    path = os.path.join(os.getcwd(), project_name)
    os.makedirs(path)
    os.chdir(project_name)
    for dir in directories:
        os.makedirs(dir)

    if tests:
        path = os.path.join(os.getcwd(), 'tests')
        os.makedirs(path)
    
    if build:
        path = os.path.join(os.getcwd(), 'tests')
        os.makedirs(path)

    if vcpkg:
        if sys.platform.lower().startswith('win'):
            os.chdir('C:/')
            os.makedirs('src/')
            os.chdir('C:/src')
            subprocess.run(['git', 'clone', 'https://github.com/Microsoft/vcpkg.git'])
        else:
            os.chdir('/home')
            os.makedirs('src/')
            os.chdir('~/src')
            subprocess.run(['git', 'clone', 'https://github.com/Microsoft/vcpkg.git'])