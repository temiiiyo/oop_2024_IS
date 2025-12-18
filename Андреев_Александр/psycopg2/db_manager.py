import psycopg2
from config import db_server, db_log, db_pass, db_port, db_database
from exceptions import DatabaseError, AuthenticationError
from models import User, Transaction


class DatabaseManager:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host=db_server,
                dbname=db_database,
                user=db_log,
                password=db_pass,
                port=db_port,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise DatabaseError("Ошибка подключения к базе данных", e)

    def login_user(self, username: str, password: str) -> User:
        try:
            self.cursor.execute(
                "SELECT user_id, role_id FROM Users WHERE username = %s AND password_hash = %s",
                (username, password),
            )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationError("Неверный логин или пароль")
            user_id, role_id = result
            return User(user_id=user_id, username=username, role_id=role_id)
        except Exception as e:
            raise DatabaseError("Ошибка выполнения входа", e)

    def fetch_transactions(self) -> list[Transaction]:
        try:
            self.cursor.execute("""
                SELECT t.transaction_id, cl.full_name, curr.name, t.amount, (t.amount * curr.sale_rate) AS total_rub
                FROM Transactions t
                JOIN Clients cl ON t.client_id = cl.client_id
                JOIN Currency curr ON t.currency_id = curr.currency_id
            """)
            results = self.cursor.fetchall()
            return [
                Transaction(
                    transaction_id=row[0],
                    client_name=row[1],
                    currency_name=row[2],
                    amount=row[3],
                    total_in_rub=row[4],
                )
                for row in results
            ]
        except Exception as e:
            raise DatabaseError("Ошибка получения данных о сделках", e)

    def fetch_clients(self):
        """Получение списка клиентов (id и имя)."""
        try:
            self.cursor.execute("SELECT client_id, full_name FROM Clients")
            return self.cursor.fetchall()
        except Exception as e:
            raise DatabaseError("Ошибка получения списка клиентов", e)

    def fetch_currencies(self):
        """Получение списка валют (id и название)."""
        try:
            self.cursor.execute("SELECT currency_id, name FROM Currency")
            return self.cursor.fetchall()
        except Exception as e:
            raise DatabaseError("Ошибка получения списка валют", e)

    def add_transaction(self, client_id, currency_id, amount):
        """Добавление новой транзакции."""
        try:
            self.cursor.execute(
                "INSERT INTO Transactions (client_id, currency_id, amount) VALUES (%s, %s, %s)",
                (client_id, currency_id, amount),
            )
            self.connection.commit()
        except Exception as e:
            raise DatabaseError("Ошибка добавления транзакции", e)
        
    def fetch_currency_share(self):
        """Получение данных из представления CurrencyShare."""
        try:
            self.cursor.execute("SELECT * FROM CurrencyShare")
            return self.cursor.fetchall()
        except Exception as e:
            raise DatabaseError("Ошибка получения данных из CurrencyShare", e)

    def fetch_max_transaction(self):
        """Получение данных из представления MaxTransaction."""
        try:
            self.cursor.execute("SELECT * FROM MaxTransaction")
            return self.cursor.fetchone()
        except Exception as e:
            raise DatabaseError("Ошибка получения данных из MaxTransaction", e)

    def close(self):
        self.cursor.close()
        self.connection.close()
