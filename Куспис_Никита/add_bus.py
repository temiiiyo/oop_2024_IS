# Добавление автобуса
import mysql.connector
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox

class AddBusDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Добавить автобус")

        layout = QFormLayout()

        self.bus_brand_input = QLineEdit(self)
        layout.addRow("Марка автобуса:", self.bus_brand_input)

        self.bus_number_input = QLineEdit(self)
        layout.addRow("Номер автобуса:", self.bus_number_input)

        self.capacity_input = QLineEdit(self)
        layout.addRow("Вместимость автобуса:", self.capacity_input)

        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_bus)
        layout.addRow(self.add_button)

        self.setLayout(layout)

    def add_bus(self):
        brand = self.bus_brand_input.text()
        number = self.bus_number_input.text()
        capacity = self.capacity_input.text()

        if brand and number and capacity:
            try:
                cursor = self.parent().cursor
                cursor.execute("INSERT INTO buses (bus_brand, bus_number, capacity) VALUES (%s, %s, %s)",
                               (brand, number, int(capacity)))
                self.parent().db.commit()
                QMessageBox.information(self, "Успех", "Автобус добавлен успешно!")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Ошибка", f"Ошибка добавления автобуса: {err}")
            self.accept()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
