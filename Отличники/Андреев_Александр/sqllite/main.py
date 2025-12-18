import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QTableWidget, QTableWidgetItem, QFileDialog, QComboBox
from PyQt6.QtCore import Qt
from db_manager import DatabaseManager
from exceptions import DatabaseError, AuthenticationError
from openpyxl import Workbook


class LoginWindow(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Вход")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout()

        self.label_username = QLabel("Имя пользователя:")
        self.input_username = QLineEdit()
        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.input_username)

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)

        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.login)
        self.layout.addWidget(self.button_login)

        self.setLayout(self.layout)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        try:
            user = self.db_manager.login_user(username, password)
            if user.role_id == 1:  # Оператор
                self.accept()
                self.main_window = OperatorWindow(self.db_manager)
                self.main_window.show()
            elif user.role_id == 2:  # Пользователь
                self.accept()
                self.main_window = UserWindow(self.db_manager)
                self.main_window.show()
        except AuthenticationError as e:
            QMessageBox.warning(self, "Ошибка входа", str(e))
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", str(e))


class UserWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Пользователь - Просмотр сделок")
        self.setGeometry(200, 200, 800, 500)

        self.table = QTableWidget(self)
        self.table.setGeometry(10, 10, 780, 450)

        self.load_data()

    def load_data(self):
        try:
            transactions = self.db_manager.fetch_transactions()
            self.table.setRowCount(len(transactions))
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(
                ["ID", "Клиент", "Валюта", "Сумма", "Итого (RUB)"]
            )

            # Устанавливаем ширину колонок
            self.table.setColumnWidth(0, 50)  # ID
            self.table.setColumnWidth(1, 200)  # Клиент
            self.table.setColumnWidth(2, 100)  # Валюта
            self.table.setColumnWidth(3, 150)  # Сумма
            self.table.setColumnWidth(4, 150)  # Итого

            for row_idx, transaction in enumerate(transactions):
                self.table.setItem(row_idx, 0, QTableWidgetItem(str(transaction.transaction_id)))
                self.table.setItem(row_idx, 1, QTableWidgetItem(transaction.client_name))
                self.table.setItem(row_idx, 2, QTableWidgetItem(transaction.currency_name))
                self.table.setItem(row_idx, 3, QTableWidgetItem(f"{transaction.amount:.2f}"))
                self.table.setItem(row_idx, 4, QTableWidgetItem(f"{transaction.total_in_rub:.2f}"))
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", str(e))


class OperatorWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Оператор - Управление сделками")
        self.setGeometry(100, 100, 850, 700)

        # Таблица для отображения операций
        self.table_transactions = QTableWidget(self)
        self.table_transactions.setGeometry(10, 10, 830, 200)

        # Таблица для отображения CurrencyShare
        self.table_currency_share = QTableWidget(self)
        self.table_currency_share.setGeometry(10, 220, 830, 150)

        # Таблица для отображения MaxTransaction
        self.table_max_transaction = QTableWidget(self)
        self.table_max_transaction.setGeometry(10, 380, 830, 100)

        # Кнопки
        self.button_add_transaction = QPushButton("Добавить операцию", self)
        self.button_add_transaction.setGeometry(10, 490, 180, 40)
        self.button_add_transaction.clicked.connect(self.add_transaction)

        self.button_export = QPushButton("Экспортировать в Excel", self)
        self.button_export.setGeometry(200, 490, 180, 40)
        self.button_export.clicked.connect(self.export_to_excel)

        self.button_refresh = QPushButton("Обновить данные", self)
        self.button_refresh.setGeometry(390, 490, 180, 40)
        self.button_refresh.clicked.connect(self.load_data)

        self.load_data()

    def load_data(self):
        # Загрузка сделок
        try:
            transactions = self.db_manager.fetch_transactions()
            self.table_transactions.setRowCount(len(transactions))
            self.table_transactions.setColumnCount(5)
            self.table_transactions.setHorizontalHeaderLabels(
                ["ID", "Клиент", "Валюта", "Сумма", "Итого (RUB)"]
            )
            self.table_transactions.setColumnWidth(0, 50)
            self.table_transactions.setColumnWidth(1, 200)
            self.table_transactions.setColumnWidth(2, 100)
            self.table_transactions.setColumnWidth(3, 150)
            self.table_transactions.setColumnWidth(4, 150)

            for row_idx, transaction in enumerate(transactions):
                self.table_transactions.setItem(row_idx, 0, QTableWidgetItem(str(transaction.transaction_id)))
                self.table_transactions.setItem(row_idx, 1, QTableWidgetItem(transaction.client_name))
                self.table_transactions.setItem(row_idx, 2, QTableWidgetItem(transaction.currency_name))
                self.table_transactions.setItem(row_idx, 3, QTableWidgetItem(f"{transaction.amount:.2f}"))
                self.table_transactions.setItem(row_idx, 4, QTableWidgetItem(f"{transaction.total_in_rub:.2f}"))
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", str(e))

        # Загрузка CurrencyShare
        try:
            currency_share = self.db_manager.fetch_currency_share()
            self.table_currency_share.setRowCount(len(currency_share))
            self.table_currency_share.setColumnCount(3)
            self.table_currency_share.setHorizontalHeaderLabels(
                ["Валюта", "Объем (RUB)", "Доля %"]
            )
            self.table_currency_share.setColumnWidth(0, 100)
            self.table_currency_share.setColumnWidth(1, 150)
            self.table_currency_share.setColumnWidth(2, 100)

            for row_idx, row in enumerate(currency_share):
                self.table_currency_share.setItem(row_idx, 0, QTableWidgetItem(row['currency_name']))
                self.table_currency_share.setItem(row_idx, 1, QTableWidgetItem(f"{row['total_volume_rub']:.2f}"))
                self.table_currency_share.setItem(row_idx, 2, QTableWidgetItem(f"{row['share'] * 100:.2f}%"))
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", str(e))

        # Загрузка MaxTransaction
        try:
            max_transaction = self.db_manager.fetch_max_transaction()
            self.table_max_transaction.setRowCount(1)
            self.table_max_transaction.setColumnCount(4)
            self.table_max_transaction.setHorizontalHeaderLabels(
                ["ID", "Клиент", "Валюта", "Итого (RUB)"]
            )
            self.table_max_transaction.setColumnWidth(0, 50)
            self.table_max_transaction.setColumnWidth(1, 200)
            self.table_max_transaction.setColumnWidth(2, 100)
            self.table_max_transaction.setColumnWidth(3, 150)

            if max_transaction:
                self.table_max_transaction.setItem(0, 0, QTableWidgetItem(str(max_transaction[0])))
                self.table_max_transaction.setItem(0, 1, QTableWidgetItem(max_transaction[1]))
                self.table_max_transaction.setItem(0, 2, QTableWidgetItem(max_transaction[2]))
                self.table_max_transaction.setItem(0, 3, QTableWidgetItem(f"{max_transaction[3]:.2f}"))
            else:
                self.table_max_transaction.setItem(0, 0, QTableWidgetItem("Нет данных"))
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", str(e))

    def add_transaction(self):
        dialog = AddTransactionDialog(self.db_manager)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()

    def export_to_excel(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "сделки.xlsx", "Excel Files (*.xlsx)")
            if file_path:
                transactions = self.db_manager.fetch_transactions()
                wb = Workbook()
                ws = wb.active
                ws.title = "Сделки"

                # Заголовки таблицы
                headers = ["ID", "Клиент", "Валюта", "Сумма", "Итого (RUB)"]
                ws.append(headers)

                # Заполнение данных
                for transaction in transactions:
                    ws.append([
                        transaction.transaction_id,
                        transaction.client_name,
                        transaction.currency_name,
                        transaction.amount,
                        transaction.total_in_rub,
                    ])

                wb.save(file_path)
                QMessageBox.information(self, "Успех", f"Данные экспортированы в файл:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось экспортировать данные: {str(e)}")


class AddTransactionDialog(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Добавить операцию")
        self.setGeometry(300, 300, 400, 250)

        self.layout = QVBoxLayout()

        # Выпадающий список для клиента
        self.label_client = QLabel("Клиент:")
        self.combo_client = QComboBox()
        self.layout.addWidget(self.label_client)
        self.layout.addWidget(self.combo_client)

        # Выпадающий список для валюты
        self.label_currency = QLabel("Валюта:")
        self.combo_currency = QComboBox()
        self.layout.addWidget(self.label_currency)
        self.layout.addWidget(self.combo_currency)

        # Поле для суммы
        self.label_amount = QLabel("Сумма:")
        self.input_amount = QLineEdit()
        self.layout.addWidget(self.label_amount)
        self.layout.addWidget(self.input_amount)

        # Кнопка для добавления
        self.button_add = QPushButton("Добавить")
        self.button_add.clicked.connect(self.add_transaction)
        self.layout.addWidget(self.button_add)

        self.setLayout(self.layout)

        # Загрузка данных для выпадающих списков
        self.load_data()

    def load_data(self):
        """Загрузка клиентов и валют в выпадающие списки."""
        try:
            # Загрузка клиентов
            clients = self.db_manager.fetch_clients()
            self.combo_client.clear()
            for client_id, full_name in clients:
                self.combo_client.addItem(full_name, client_id)

            # Загрузка валют
            currencies = self.db_manager.fetch_currencies()
            self.combo_currency.clear()
            for currency_id, name in currencies:
                self.combo_currency.addItem(name, currency_id)
        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def add_transaction(self):
        """Добавление новой транзакции."""
        try:
            client_id = self.combo_client.currentData()
            currency_id = self.combo_currency.currentData()

            if not client_id or not currency_id:
                QMessageBox.warning(self, "Ошибка", "Выберите клиента и валюту")
                return

            amount_text = self.input_amount.text()
            if not amount_text:
                QMessageBox.warning(self, "Ошибка", "Введите сумму")
                return

            try:
                amount = float(amount_text)
                if amount <= 0:
                    QMessageBox.warning(self, "Ошибка", "Сумма должна быть положительным числом")
                    return

                self.db_manager.add_transaction(client_id, currency_id, amount)
                QMessageBox.information(self, "Успех", "Операция успешно добавлена")
                self.accept()
            except ValueError:
                QMessageBox.critical(self, "Ошибка", "Сумма должна быть числом")

        except DatabaseError as e:
            QMessageBox.critical(self, "Ошибка", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        db_manager = DatabaseManager()
        login_window = LoginWindow(db_manager)

        # Тестовые данные для входа:
        # Оператор: admin / admin123
        # Пользователь: user1 / user123

        if login_window.exec() == QDialog.DialogCode.Accepted:
            sys.exit(app.exec())
    except DatabaseError as e:
        QMessageBox.critical(None, "Ошибка базы данных", str(e))
        # Создаем базу данных если её нет
        try:
            import init_database

            init_database.create_database()
            QMessageBox.information(None, "Информация", "База данных создана. Перезапустите приложение.")
        except Exception as e2:
            QMessageBox.critical(None, "Критическая ошибка", f"Не удалось создать базу данных: {e2}")