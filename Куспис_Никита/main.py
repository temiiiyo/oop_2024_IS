'''
Проект "Автовокзал".. Куспис Н.С, 44ИС-21, Москва, КМПО РАНХиГС.
1. Автовокзал.
Автобусы производят рейсы до станций по расписанию. Каждый автобус вмещает не более определенного количества пассажиров
Таблицы: станции (код станции, название станции), автобусы (код автобуса, марка автобуса, государственный номер, вместимость),
рейсы (код рейса, код станции, код автобуса, время отправления).
Определить:
- сколько выполняется рейсов до каждой станции?
- каково общее количество пассажиров?
---
Решение. Куспис Н.С.
Начало решения 12.12.2024, 18:40
Окончание решения 12.12.2024, 21:50
Время выполнения: 3 часа 10 минут.
'''

import sys
import mysql.connector
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QLabel, QMessageBox
import openpyxl
from styles import MAIN_WINDOW_STYLE
from add_bus import AddBusDialog
from add_station import AddStationDialog
from add_trip_dialog import AddTripDialog
from database import get_database_connection

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Автовокзал")
        self.setGeometry(100, 100, 800, 600)

        # Подключение к базе данных
        self.db = get_database_connection()
        self.cursor = self.db.cursor()

        # Заголовок
        self.label = QLabel("Автовокзал", self)
        self.label.setGeometry(365, 10, 200, 40)

        self.label = QLabel("Доступные рейсы", self)
        self.label.setGeometry(335, 280, 200, 40)

        # Кнопки в 1-м столбике
        self.add_station_button = QPushButton("Добавить станцию", self)
        self.add_station_button.setGeometry(100, 60, 300, 40)
        self.add_station_button.clicked.connect(self.open_add_station_dialog)

        self.add_bus_button = QPushButton("Добавить автобус", self)
        self.add_bus_button.setGeometry(100, 110, 300, 40)
        self.add_bus_button.clicked.connect(self.open_add_bus_dialog)

        self.add_trip_button = QPushButton("Добавить рейс", self)
        self.add_trip_button.setGeometry(100, 160, 300, 40)
        self.add_trip_button.clicked.connect(self.open_add_trip_dialog)

        # Кнопки во 2-м столбике
        self.view_trips_button = QPushButton("Вывести рейсы", self)
        self.view_trips_button.setGeometry(450, 60, 300, 40)
        self.view_trips_button.clicked.connect(self.show_trips)

        self.trip_count_button = QPushButton("Количество рейсов до каждой станции", self)
        self.trip_count_button.setGeometry(450, 110, 300, 40)
        self.trip_count_button.clicked.connect(self.show_trip_count)

        self.total_passengers_button = QPushButton("Общее количество пассажиров", self)
        self.total_passengers_button.setGeometry(450, 160, 300, 40)
        self.total_passengers_button.clicked.connect(self.show_total_passengers)

        # Экспорт в Excel
        self.export_to_excel_button = QPushButton("Экспорт в Excel", self)
        self.export_to_excel_button.setGeometry(100, 210, 650, 40)
        self.export_to_excel_button.clicked.connect(self.export_to_excel)

        # Таблица для отображения данных
        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setGeometry(100, 320, 650, 200)
        self.table.setHorizontalHeaderLabels(["Код", "Станция", "Марка автобуса", "Номер автобуса", "Время отправления"])

        self.setStyleSheet(MAIN_WINDOW_STYLE)

    # Открытие диалога для добавления станции
    def open_add_station_dialog(self):
        dialog = AddStationDialog(self)
        dialog.exec()

    # Открытие диалога для добавления автобуса
    def open_add_bus_dialog(self):
        dialog = AddBusDialog(self)
        dialog.exec()

    # Открытие диалога для добавления рейса
    def open_add_trip_dialog(self):
        dialog = AddTripDialog(self)
        dialog.exec()

    # Показать рейсы и общее количество мест
    def show_trips(self):
        try:
            query = """
            SELECT t.trip_id, s.station_name, b.bus_brand, b.bus_number, t.departure_time
            FROM trips t
            JOIN stations s ON t.station_id = s.station_id
            JOIN buses b ON t.bus_id = b.bus_id
            """
            self.cursor.execute(query)
            trips = self.cursor.fetchall()

            # Очистка таблицы перед выводом новых данных
            self.table.setRowCount(0)

            # Заполнение таблицы рейсами
            for row_num, trip in enumerate(trips):
                self.table.insertRow(row_num)
                for col_num, data in enumerate(trip):
                    self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Ошибка подключения: {err}")

    # Количество рейсов до каждой станции
    def show_trip_count(self):
        try:
            query = """
            SELECT s.station_name, COUNT(t.trip_id) AS trip_count
            FROM stations s
            LEFT JOIN trips t ON s.station_id = t.station_id
            GROUP BY s.station_id;
            """
            self.cursor.execute(query)
            trips = self.cursor.fetchall()

            result = "Количество рейсов до каждой станции:\n"
            for station_name, trip_count in trips:
                result += f"{station_name}: {trip_count} рейсов\n"

            QMessageBox.information(self, "Рейсы", result)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Ошибка подключения: {err}")

    # Общее количество пассажиров
    def show_total_passengers(self):
        try:
            query = """
            SELECT SUM(b.capacity) AS total_capacity
            FROM trips t
            JOIN buses b ON t.bus_id = b.bus_id;
            """
            self.cursor.execute(query)
            total_passengers = self.cursor.fetchone()[0]

            QMessageBox.information(self, "Общее количество пассажиров", f"Общее количество мест для пассажиров: {total_passengers}")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Ошибка подключения: {err}")

    # Экспорт рейсов в Excel
    def export_to_excel(self):
        try:
            query = """
            SELECT t.trip_id, s.station_name, b.bus_brand, b.bus_number, t.departure_time
            FROM trips t
            JOIN stations s ON t.station_id = s.station_id
            JOIN buses b ON t.bus_id = b.bus_id
            """
            self.cursor.execute(query)
            trips = self.cursor.fetchall()

            # Создаем новый Excel файл
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = "Рейсы"

            # Заголовки столбцов
            sheet.append(["Код", "Станция", "Марка автобуса", "Номер автобуса", "Время отправления"])

            # Заполнение данными
            for trip in trips:
                sheet.append(trip)

            # Сохранение файла
            file_path = "trips.xlsx"
            wb.save(file_path)

            QMessageBox.information(self, "Экспорт в Excel", f"Данные экспортированы в {file_path}")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при экспорте данных: {err}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при экспорте данных: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
