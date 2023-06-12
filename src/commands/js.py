import typer
import subprocess
from typing_extensions import Annotated
import sys
from libs.lib import AppError

app = typer.Typer()

@app.command()
def init(
    npm: Annotated[bool, typer.Option(help='Se você quiser usar o npm use essa opção')] = False,
    yarn: Annotated[bool, typer.Option(help='Se você quiser usar o yarn use essa opção (Não é necessário já ter instalado)')] = False,
    pnpm: Annotated[bool, typer.Option(help='Se você quiser usar o pnpm use essa opção (Não é necessário já ter instalado)')] = False,
    docker: Annotated[bool, typer.Option(help='Cria um docker compose')] = False
) -> None:
    
    if npm:
        if sys.platform.lower().startswith('win'):
            subprocess.run('npm.cmd create vite@latest')
        else:
            subprocess.run(['npm', 'create', 'vite@latest'])
    
    if yarn:
        if sys.platform.lower().startswith('win'):
            try:
                subprocess.run(['yarn.cmd', 'create', 'vite'])
            except FileNotFoundError:
                AppError('Você não tem o yarn instalado, instalando....')
                subprocess.run('npm.cmd install --global yarn')
                subprocess.run(['powershell.exe', '-NoExit', 'yarn.cmd', 'create', 'vite'])  
        else:
            try:
                subprocess.run(['yarn', 'create', 'vite'])
            except FileNotFoundError:
                AppError('Você não tem o yarn instalado, instalando....')
                subprocess.run('npm', 'install', '--global', 'yarn')
                subprocess.run(['exec', '$SHELL', 'yarn', 'create', 'vite']) 
            
    if pnpm:
        if sys.platform.lower().startswith('win'):
            try:
                subprocess.run(['pnpm', 'create', 'vite'])
            except FileNotFoundError:
                AppError('Você não tem o pnpm instalado, instalando....')
                subprocess.run('powershell.exe iwr https://get.pnpm.io/install.ps1 -useb | iex')
                subprocess.run(['powershell.exe', '-NoExit', 'pnpm', 'create', 'vite'])   
        else:
            try:
                subprocess.run(['pnpm', 'create', 'vite'])
            except FileNotFoundError:
                AppError('Você não tem o pnpm instalado, instalando....')
                subprocess.run(['curl', '-fsSL', 'https://get.pnpm.io/install.sh', '|', 'sh', '-'])
                subprocess.run(['exec', '$SHELL', 'pnpm', 'create', 'vite'])

    if docker:
        with open('docker-compose.yml', 'w') as file:
            file.write('version: "3.4"\n\nservices:\n vite_docker:\n image: node:alpine\n container_name: vite\n entrypoint: /bin/sh\n ports:\n - 8000:8000\n working_dir: /srv/app\n volumes:\n - type: bind\n source: ./\n target: /srv/app\ntty: true')

                    