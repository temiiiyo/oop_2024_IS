import sys
from bd import execute_query, fetch_data
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QComboBox, QFormLayout, QLineEdit, QMessageBox)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from openpyxl import Workbook


# Основное окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Междугородная телефонная станция")
        self.setGeometry(200, 200, 800, 800)

        self.layout = QVBoxLayout()

        # Таблица для отображения разговоров
        self.table_conversations = QTableWidget(self)
        self.layout.addWidget(self.table_conversations)

        # Круговая диаграмма для отображения доли стоимости по городам
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Кнопка для добавления записи
        self.add_button = QPushButton("Добавить запись", self)
        self.add_button.clicked.connect(self.show_add_form)
        self.layout.addWidget(self.add_button)

        # Кнопка для выгрузки данных в Excel
        self.export_button = QPushButton("Выгрузить данные в Excel", self)
        self.export_button.clicked.connect(self.export_to_excel)
        self.layout.addWidget(self.export_button)

        self.setLayout(self.layout)

        # Загрузка данных сразу при инициализации окна
        self.load_data()

    def load_data(self):
        # Запрос 1: Список разговоров в порядке возрастания времени начала
        self.query_conversations = """
            SELECT 
                c.call_id, 
                ci.name, 
                ci.distance AS city_distance, 
                c.start_time, 
                c.duration, 
                t.price 
            FROM calls c
            JOIN cities ci ON c.city_id = ci.city_id
            JOIN tariffs t ON ci.tariff_id = t.tariff_id
            ORDER BY c.start_time;
        """
        self.conversations = fetch_data(self.query_conversations)

        # Заполнение таблицы разговоров
        self.table_conversations.setRowCount(len(self.conversations))
        self.table_conversations.setColumnCount(6)
        self.table_conversations.setHorizontalHeaderLabels([
            "ID Разговора", "Город", "Расстояние", "Время начала", "Продолжительность (мин)", "Цена (руб)"
        ])

        for i, row in enumerate(self.conversations):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.table_conversations.setItem(i, j, item)

        # Запрос 2: Доля стоимости разговоров по каждому городу
        self.query_city_cost = """
            WITH CityCosts AS (
                SELECT 
                    ci.name,
                    SUM(c.duration * t.price) AS city_cost -- Стоимость разговоров по каждому городу
                FROM calls c
                JOIN cities ci ON c.city_id = ci.city_id
                JOIN tariffs t ON ci.tariff_id = t.tariff_id
                GROUP BY ci.city_id
            ),
            TotalCost AS (
                SELECT SUM(c.duration * t.price) AS total_cost -- Общая стоимость всех разговоров
                FROM calls c
                JOIN cities ci ON c.city_id = ci.city_id
                JOIN tariffs t ON ci.tariff_id = t.tariff_id
            )
            SELECT 
                cc.name, 
                cc.city_cost,
                (cc.city_cost / tc.total_cost) * 100 AS city_cost_percentage
            FROM CityCosts cc, TotalCost tc
            ORDER BY city_cost_percentage;
        """
        self.city_costs = fetch_data(self.query_city_cost)

        # Построение круговой диаграммы
        city_names = [str(row[0]) for row in self.city_costs]
        city_percentages = [row[2] for row in self.city_costs]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.pie(city_percentages, labels=city_names, autopct='%1.1f%%', startangle=90)
        ax.set_title("Доля стоимости разговоров по городам")
        self.canvas.draw()

    def show_add_form(self):
        # Создаем форму для добавления записи
        self.add_form = QWidget()
        self.add_form.setWindowTitle("Добавить запись")
        layout = QFormLayout()

        # Выпадающий список для выбора города
        self.city_dropdown = QComboBox()
        cities_query = "SELECT name FROM cities;"
        cities = fetch_data(cities_query)
        for city in cities:
            self.city_dropdown.addItem(city[0])

        self.start_time_input = QLineEdit()
        self.duration_input = QLineEdit()

        layout.addRow("Город:", self.city_dropdown)
        layout.addRow("Время начала:", self.start_time_input)
        layout.addRow("Продолжительность (мин):", self.duration_input)

        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.add_record)

        layout.addWidget(save_button)
        self.add_form.setLayout(layout)
        self.add_form.show()

    def add_record(self):
        city = self.city_dropdown.currentText()
        start_time = self.start_time_input.text()
        duration = self.duration_input.text()

        # Запрос для добавления записи
        query = """
            INSERT INTO calls (city_id, start_time, duration)
            SELECT ci.city_id, ?, ?
            FROM cities ci
            WHERE ci.name = ?;
        """
        if execute_query(query, (start_time, duration, city)):
            QMessageBox.information(self, "Успех", "Запись успешно добавлена.")
            self.add_form.close()
            self.load_data()  # Обновляем таблицу
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось добавить запись.")

    def export_to_excel(self):
        wb = Workbook()

        # Лист для разговоров
        sheet1 = wb.active
        sheet1.title = "Разговоры"
        sheet1.append(["ID Разговора", "Город", "Расстояние", "Время начала", "Продолжительность (мин)", "Цена (руб)"])
        for row in self.conversations:
            sheet1.append(row)

        # Лист для доли стоимости
        sheet2 = wb.create_sheet("Доля стоимости")
        sheet2.append(["Город", "Стоимость (руб)", "Доля (%)"])
        for row in self.city_costs:
            sheet2.append(row)

        # Сохранение файла
        filename = "Междугородная_телефонная_станция.xlsx"
        wb.save(filename)
        QMessageBox.information(self, "Успех", f"Данные успешно выгружены в файл {filename}")

# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())