# Добавление рейса
import mysql.connector
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox

class AddTripDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Добавить рейс")

        layout = QFormLayout()

        self.station_name_input = QLineEdit(self)
        layout.addRow("Станция:", self.station_name_input)

        self.bus_number_input = QLineEdit(self)
        layout.addRow("Номер автобуса:", self.bus_number_input)

        self.departure_time_input = QLineEdit(self)
        layout.addRow("Время отправления:", self.departure_time_input)

        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_trip)
        layout.addRow(self.add_button)

        self.setLayout(layout)

    def add_trip(self):
        station_name = self.station_name_input.text()
        bus_number = self.bus_number_input.text()
        departure_time = self.departure_time_input.text()

        if station_name and bus_number and departure_time:
            try:
                cursor = self.parent().cursor
                cursor.execute("""
                    INSERT INTO trips (station_id, bus_id, departure_time)
                    SELECT station_id, bus_id, %s
                    FROM stations, buses
                    WHERE station_name = %s AND bus_number = %s
                """, (departure_time, station_name, bus_number))
                self.parent().db.commit()
                QMessageBox.information(self, "Успех", "Рейс добавлен успешно!")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Ошибка", f"Ошибка добавления рейса: {err}")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")