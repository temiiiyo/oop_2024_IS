from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QWidget, QComboBox
from db import connect_db, get_categories, get_expenses
from budget_calculator import calculate_monthly_budget
from excel_report import generate_excel_report
from budget_calculator import BudgetComparisonError

class BudgetApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Месячный бюджет")
        self.resize(800, 600)

        self.layout = QVBoxLayout()

        self.start_date_input = QLineEdit(self)
        self.start_date_input.setPlaceholderText("Введите дату начала (YYYY-MM-DD)")
        self.layout.addWidget(self.start_date_input)

        self.end_date_input = QLineEdit(self)
        self.end_date_input.setPlaceholderText("Введите дату окончания (YYYY-MM-DD)")
        self.layout.addWidget(self.end_date_input)

        self.calculate_button = QPushButton("Посчитать", self)
        self.calculate_button.clicked.connect(self.calculate_budget)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Результат будет отображен здесь", self)
        self.layout.addWidget(self.result_label)

        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

        self.export_button = QPushButton("Экспорт в Excel", self)
        self.export_button.clicked.connect(self.export_report)
        self.layout.addWidget(self.export_button)

        self.add_expense_label = QLabel("Добавить новую трату:", self)
        self.layout.addWidget(self.add_expense_label)

        self.category_combo = QComboBox(self)
        self.layout.addWidget(self.category_combo)

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Количество")
        self.layout.addWidget(self.quantity_input)

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Цена")
        self.layout.addWidget(self.price_input)

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Дата (YYYY-MM-DD)")
        self.layout.addWidget(self.date_input)

        self.add_expense_button = QPushButton("Добавить трату", self)
        self.add_expense_button.clicked.connect(self.add_expense)
        self.layout.addWidget(self.add_expense_button)

        central_widget = QWidget(self)
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.load_categories()

    def load_categories(self):
        try:
            conn = connect_db()
            categories = get_categories(conn)
            self.category_combo.clear()
            for category_id, category_name in categories:
                self.category_combo.addItem(category_name, userData=category_id)  # Добавляем категорию по имени
            conn.close()
        except Exception as e:
            self.result_label.setText(f"Ошибка загрузки категорий: {e}")

    def calculate_budget(self):
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()

        if not start_date or not end_date:
            self.result_label.setText("Пожалуйста, укажите даты начала и конца периода.")
            return

        try:
            conn = connect_db()

            expenses = get_expenses(conn, start_date, end_date)

            if not expenses:
                self.result_label.setText("Нет данных за указанный период.")
                return

            total_expenses, expenses_by_item, item_share = calculate_monthly_budget(expenses)

            self.result_label.setText(f"Месячный бюджет: {total_expenses:.2f} руб.")
            
            self.table.setRowCount(len(expenses_by_item))
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["Статья", "Сумма", "Доля (%)"])

            row = 0
            for item, expense in expenses_by_item.items():
                self.table.setItem(row, 0, QTableWidgetItem(item))
                self.table.setItem(row, 1, QTableWidgetItem(f"{expense:.2f}"))
                self.table.setItem(row, 2, QTableWidgetItem(f"{item_share[item]:.2f}"))
                row += 1

            self.table.resizeColumnsToContents()

            conn.close()

        except Exception as e:
            self.result_label.setText(f"Ошибка: {e}")

    def add_expense(self):
        category_id = self.category_combo.currentData()
        quantity = self.quantity_input.text()
        price = self.price_input.text()
        date = self.date_input.text()

        if not category_id or not quantity or not price or not date:
            self.result_label.setText("Пожалуйста, заполните все поля.")
            return

        try:
            conn = connect_db()
            cur = conn.cursor()

            # Вставка новой траты
            query = """
            INSERT INTO "OOOP".expense (id_categories, quantity, price, date)
            VALUES (%s, %s, %s, %s)
            """
            cur.execute(query, (category_id, float(quantity), float(price), date))
            conn.commit()

            self.result_label.setText("Трата успешно добавлена.")
            conn.close()

            self.quantity_input.clear()
            self.price_input.clear()
            self.date_input.clear()

        except Exception as e:
            self.result_label.setText(f"Ошибка добавления траты: {e}")

    def export_report(self):
        try:
            total_expenses = self.result_label.text()
            if not total_expenses.startswith("Месячный бюджет"):
                raise BudgetComparisonError("Не были произведены расчёты бюджета.")

            expenses_by_item = {}
            item_share = {}

            for row in range(self.table.rowCount()):
                item = self.table.item(row, 0).text()
                expense = float(self.table.item(row, 1).text())
                share = float(self.table.item(row, 2).text())
                expenses_by_item[item] = expense
                item_share[item] = share

            generate_excel_report(expenses_by_item, item_share, total_expenses)
            self.result_label.setText("Отчет успешно экспортирован в Excel.")

        except Exception as e:
            self.result_label.setText(f"Ошибка при экспорте: {e}")
