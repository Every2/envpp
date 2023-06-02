class AppError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(print(message))
        self.isAppError = True
         