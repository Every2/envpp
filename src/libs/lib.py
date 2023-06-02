import os

class AppError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(print(message))
        self.isAppError = True

class FirstExecutionChecker:
    def __init__(self, flag = "flag.json") -> None:
        self.flag = flag

    def check_first_execution(self) -> None:
        if os.path.isfile(self.flag):
            AppError('Você já rodou o script antes, use --help para ver os commandos')
        else:
            with open(self.flag, 'w') as f:
                f.write('Sua primeira vez. :)')
            return print('Configurando o ambiente para você')
        