class Customer:
    """
    Класс, представляющий клиента.

    Атрибуты:
        id (int): Идентификатор клиента.
        name (str): Имя клиента.
        email (str): Электронная почта клиента.
    """

    def __init__(self, id, name, email):
        """
        Инициализация нового клиента.

        Аргументы:
            id (int): Идентификатор клиента.
            name (str): Имя клиента.
            email (str): Электронная почта клиента.
        """
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        """
        Строковое представление клиента.

        Возвращает:
            str: Строка с информацией о клиенте.
        """
        return f"Клиент(ID: {self.id}, Имя: {self.name}, Email: {self.email})"

    def update_email(self, new_email):
        """
        Обновить email клиента.

        Аргументы:
            new_email (str): Новый email клиента.
        """
        self.email = new_email
        print(f"Email обновлен на: {self.email}")

    def get_full_info(self):
        """
        Получить полную информацию о клиенте.

        Возвращает:
            str: Полная информация о клиенте.
        """
        return f"Клиент ID: {self.id}, Имя: {self.name}, Email: {self.email}"
