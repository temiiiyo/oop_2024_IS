# Добавление станции
import mysql.connector
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox

class AddStationDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Добавить станцию")

        layout = QFormLayout()

        self.station_name_input = QLineEdit(self)
        layout.addRow("Название станции:", self.station_name_input)

        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_station)
        layout.addRow(self.add_button)

        self.setLayout(layout)

    def add_station(self):
        name = self.station_name_input.text()
        if name:
            try:
                cursor = self.parent().cursor
                cursor.execute("INSERT INTO stations (station_name) VALUES (%s)", (name,))
                self.parent().db.commit()
                QMessageBox.information(self, "Успех", "Станция добавлена успешно!")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Ошибка", f"Ошибка добавления станции: {err}")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите название станции.")