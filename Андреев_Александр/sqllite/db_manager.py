import sqlite3
from exceptions import DatabaseError, AuthenticationError
from models import User, Transaction


class DatabaseManager:
    def __init__(self):
        try:
            self.connection = sqlite3.connect('bank.db')
            self.connection.row_factory = sqlite3.Row  # Для доступа к полям по имени
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise DatabaseError("Ошибка подключения к базе данных", e)

    def login_user(self, username: str, password: str) -> User:
        try:
            self.cursor.execute(
                "SELECT user_id, role_id FROM Users WHERE username = ? AND password_hash = ?",
                (username, password)
            )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationError("Неверный логин или пароль")
            user_id = result['user_id']
            role_id = result['role_id']
            return User(user_id=user_id, username=username, role_id=role_id)
        except Exception as e:
            raise DatabaseError("Ошибка выполнения входа", e)

    def fetch_transactions(self) -> list[Transaction]:
        try:
            self.cursor.execute("""
                SELECT 
                    t.transaction_id, 
                    cl.full_name, 
                    curr.name, 
                    t.amount, 
                    (t.amount * curr.sale_rate) AS total_rub
                FROM Transactions t
                JOIN Clients cl ON t.client_id = cl.client_id
                JOIN Currency curr ON t.currency_id = curr.currency_id
                ORDER BY t.transaction_date DESC
            """)
            results = self.cursor.fetchall()
            return [
                Transaction(
                    transaction_id=row['transaction_id'],
                    client_name=row['full_name'],
                    currency_name=row['name'],
                    amount=row['amount'],
                    total_in_rub=row['total_rub']
                )
                for row in results
            ]
        except Exception as e:
            raise DatabaseError("Ошибка получения данных о сделках", e)

    def fetch_clients(self):
        """Получение списка клиентов (id и имя)."""
        try:
            self.cursor.execute("SELECT client_id, full_name FROM Clients ORDER BY full_name")
            return [(row['client_id'], row['full_name']) for row in self.cursor.fetchall()]
        except Exception as e:
            raise DatabaseError("Ошибка получения списка клиентов", e)

    def fetch_currencies(self):
        """Получение списка валют (id и название)."""
        try:
            self.cursor.execute("SELECT currency_id, name FROM Currency ORDER BY name")
            return [(row['currency_id'], row['name']) for row in self.cursor.fetchall()]
        except Exception as e:
            raise DatabaseError("Ошибка получения списка валют", e)

    def add_transaction(self, client_id, currency_id, amount):
        """Добавление новой транзакции."""
        try:
            self.cursor.execute(
                "INSERT INTO Transactions (client_id, currency_id, amount) VALUES (?, ?, ?)",
                (client_id, currency_id, amount)
            )
            self.connection.commit()
        except Exception as e:
            raise DatabaseError("Ошибка добавления транзакции", e)

    def fetch_currency_share(self):
        """Получение данных из представления CurrencyShare."""
        try:
            self.cursor.execute("SELECT * FROM CurrencyShare ORDER BY total_volume_rub DESC")
            return self.cursor.fetchall()
        except Exception as e:
            raise DatabaseError("Ошибка получения данных из CurrencyShare", e)

    def fetch_max_transaction(self):
        """Получение данных из представления MaxTransaction."""
        try:
            self.cursor.execute("SELECT * FROM MaxTransaction")
            result = self.cursor.fetchone()
            if result:
                return (
                    result['transaction_id'],
                    result['client_name'],
                    result['currency_name'],
                    result['total_rub']
                )
            return None
        except Exception as e:
            raise DatabaseError("Ошибка получения данных из MaxTransaction", e)

    def close(self):
        self.cursor.close()
        self.connection.close()