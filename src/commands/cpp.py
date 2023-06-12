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
    docker: Annotated[bool, typer.Option(help='Cria um dockerfile simples')] = False
) -> None:
    directories = ['src', 'include', 'lib', 'bin']
    path = os.path.join(os.getcwd(), project_name)
    os.makedirs(path)
    os.chdir(project_name)
    for dir in directories:
        os.makedirs(dir)
        with open('CMakeLists.txt', 'w') as f:
            f.write("")
        
        if dir == 'src':
            with open('src\main.cpp', "w") as f:
                f.write("")
        
        if dir == 'include':
            with open('include\class.hpp', "w") as f:
                f.write("")

    if tests:
        path = os.path.join(os.getcwd(), 'tests')
        os.makedirs(path)
        with open('tests/test.cpp', "w") as f:
                f.write("")
    
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

    if docker:
        with open('Dockerfile', 'w') as file:
            file.write('FROM mcr.microsoft.com/devcontainers/cpp\n\nRUN mkdir app\n\nWORKDIR /app\n\n')