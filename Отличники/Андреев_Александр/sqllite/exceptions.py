class DatabaseError(Exception):
    """Исключение для ошибок базы данных"""

    def __init__(self, message: str, original_exception: Exception = None):
        super().__init__(message)
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.args[0]} (Оригинальная ошибка: {self.original_exception})"
        return self.args[0]


class AuthenticationError(Exception):
    """Исключение для ошибок аутентификации"""

    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        return f"Аутентификация не выполнена: {self.args[0]}"
