import typer
import subprocess
import sys
from libs.lib import FirstExecutionChecker

app = typer.Typer()
first_time = FirstExecutionChecker()

if first_time.check_first_execution():
   if sys.platform.startswith("win"):
       subprocess.run('npm.cmd install --global yarn')
       subprocess.run(['pip', 'install', '--user', 'pdm'])
   else:
       subprocess.run(['npm', 'install', '--global', 'yarn'])
       subprocess.run(['pip', 'install', '--user', 'pdm'])
    
@app.command()
def aaa():
    ...

if __name__  == '__main__':
    app()
