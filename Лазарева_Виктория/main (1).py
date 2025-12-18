#Лазарева Виктория 44ИС-21 11вариант

import mysql.connector
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QComboBox,
                             QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QLineEdit, QStackedWidget,
                             QMessageBox, QFormLayout, QTableWidget, QTableWidgetItem)
from PyQt6.QtGui import QFont

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кинотеатр - Вход")
        self.setFixedSize(400, 300)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.username_label = QLabel("Имя пользователя:")
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: #6F4E37;")
        self.username_input = QLineEdit()
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("border: 2px solid #A0522D; border-radius: 10px; padding: 5px;")

        self.password_label = QLabel("Пароль:")
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: #6F4E37;")
        self.password_input = QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("border: 2px solid #A0522D; border-radius: 10px; padding: 5px;")

        self.login_button = QPushButton("Войти")
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: #B22222; color: white; border-radius: 10px; padding: 10px;")
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Регистрация")
        self.register_button.setFont(font)
        self.register_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.register_button.clicked.connect(self.register)

        self.info_label = QLabel("")
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("color: #B22222;")

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.info_label)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        db = self.connect_to_db()
        if not db:
            self.info_label.setText("Ошибка подключения к базе данных.")
            return

        cursor = db.cursor()
        cursor.execute("SELECT Role FROM Users WHERE Username=%s AND Password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            role = result[0]
            if role == "User":
                self.open_user_window()
            elif role == "Admin":
                self.open_admin_window()
        else:
            self.info_label.setText("Неверное имя пользователя или пароль.")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        db = self.connect_to_db()
        if not db:
            self.info_label.setText("Ошибка подключения к базе данных.")
            return

        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Users (Username, Password, Role) VALUES (%s, %s, 'User')", (username, password))
            db.commit()
            self.info_label.setStyleSheet("color: #228B22;")
            self.info_label.setText("Регистрация успешна.")
        except mysql.connector.Error as e:
            self.info_label.setText(f"Ошибка регистрации: {e}")

    def connect_to_db(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="CinemaBASAA"
            )
        except mysql.connector.Error:
            return None

    def open_user_window(self):
        self.user_window = CinemaApp()
        self.user_window.show()
        self.close()

    def open_admin_window(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.close()


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кинотеатр - Администратор")
        self.setFixedSize(800, 600)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.add_movie_button = QPushButton("Добавить фильм")
        self.add_movie_button.setFont(font)
        self.add_movie_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.add_movie_button.clicked.connect(self.add_movie)

        self.manage_sessions_button = QPushButton("Управление сеансами")
        self.manage_sessions_button.setFont(font)
        self.manage_sessions_button.setStyleSheet("background-color: #6F4E37; color: white; border-radius: 10px; padding: 10px;")
        self.manage_sessions_button.clicked.connect(self.manage_sessions)

        self.manage_halls_button = QPushButton("Управление залами")
        self.manage_halls_button.setFont(font)
        self.manage_halls_button.setStyleSheet("background-color: #A0522D; color: white; border-radius: 10px; padding: 10px;")
        self.manage_halls_button.clicked.connect(self.manage_halls)

        self.back_button = QPushButton("Назад")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: #B22222; color: white; border-radius: 10px; padding: 10px;")
        self.back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.add_movie_button)
        layout.addWidget(self.manage_sessions_button)
        layout.addWidget(self.manage_halls_button)
        layout.addWidget(self.back_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_movie(self):
        self.add_movie_window = AddMovieWindow()
        self.add_movie_window.show()

    def manage_sessions(self):
        self.manage_sessions_window = ManageSessionsWindow()
        self.manage_sessions_window.show()

    def manage_halls(self):
        self.manage_halls_window = ManageHallsWindow()
        self.manage_halls_window.show()


class AddMovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить фильм")
        self.setFixedSize(400, 150)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.title_input = QLineEdit()
        self.title_input.setFont(font)
        self.title_input.setPlaceholderText("Название фильма")

        self.genre_input = QLineEdit()
        self.genre_input.setFont(font)
        self.genre_input.setPlaceholderText("Жанр")

        self.add_button = QPushButton("Добавить")
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.add_button.clicked.connect(self.add_movie_to_db)

        layout = QFormLayout()
        layout.addRow("Название:", self.title_input)
        layout.addRow("Жанр:", self.genre_input)
        layout.addRow(self.add_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_movie_to_db(self):
        title = self.title_input.text()
        genre = self.genre_input.text()

        if not (title and genre):
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="CinemaBASAA"
            )
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO Movie (Title, Genre) VALUES (%s, %s)",
                (title, genre)
            )
            db.commit()
            QMessageBox.information(self, "Успех", "Фильм успешно добавлен!")
            self.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить фильм: {e}")


class ManageSessionsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление сеансами")
        self.setFixedSize(600, 400)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.session_table = QTableWidget()
        self.session_table.setColumnCount(4)
        self.session_table.setHorizontalHeaderLabels(["Фильм", "Дата", "Время", "Зал"])
        self.session_table.setFont(font)

        self.add_session_button = QPushButton("Добавить сеанс")
        self.add_session_button.setFont(font)
        self.add_session_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.add_session_button.clicked.connect(self.add_session)

        self.back_button = QPushButton("Назад")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: #B22222; color: white; border-radius: 10px; padding: 10px;")
        self.back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.session_table)
        layout.addWidget(self.add_session_button)
        layout.addWidget(self.back_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_session(self):
        self.add_session_window = AddSessionWindow()
        self.add_session_window.show()


class AddSessionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить сеанс")
        self.setFixedSize(400, 300)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.movie_input = QLineEdit()
        self.movie_input.setFont(font)
        self.movie_input.setPlaceholderText("Название фильма")

        self.date_input = QLineEdit()
        self.date_input.setFont(font)
        self.date_input.setPlaceholderText("Дата (ГГГГ-ММ-ДД)")

        self.time_input = QLineEdit()
        self.time_input.setFont(font)
        self.time_input.setPlaceholderText("Время (ЧЧ:ММ:СС)")

        self.hall_input = QLineEdit()
        self.hall_input.setFont(font)
        self.hall_input.setPlaceholderText("Зал")

        self.add_button = QPushButton("Добавить")
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.add_button.clicked.connect(self.add_session_to_db)

        layout = QFormLayout()
        layout.addRow("Фильм:", self.movie_input)
        layout.addRow("Дата:", self.date_input)
        layout.addRow("Время:", self.time_input)
        layout.addRow("Зал:", self.hall_input)
        layout.addRow(self.add_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_session_to_db(self):
        movie = self.movie_input.text()
        date = self.date_input.text()
        time = self.time_input.text()
        hall = self.hall_input.text()

        if not (movie and date and time and hall):
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="CinemaBASAA"
            )
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO Sessions (MovieID, ShowTime, HallID) VALUES ((SELECT MovieID FROM Movie WHERE Title = %s), CONCAT(%s, ' ', %s), %s)",
                (movie, date, time, hall)
            )
            db.commit()
            QMessageBox.information(self, "Успех", "Сеанс успешно добавлен!")
            self.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить сеанс: {e}")


class ManageHallsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление залами")
        self.setFixedSize(600, 400)
        self.initUI()

    def initUI(self):
        font = QFont("Montserrat", 12)

        self.halls_table = QTableWidget()
        self.halls_table.setColumnCount(3)
        self.halls_table.setHorizontalHeaderLabels(["Зал", "Вместимость", "Процент заполнения"])
        self.halls_table.setFont(font)

        self.refresh_button = QPushButton("Обновить данные")
        self.refresh_button.setFont(font)
        self.refresh_button.setStyleSheet("background-color: #6F4E37; color: white; border-radius: 10px; padding: 10px;")
        self.refresh_button.clicked.connect(self.load_hall_statistics)

        self.back_button = QPushButton("Назад")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: #8B4513; color: white; border-radius: 10px; padding: 10px;")
        self.back_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.halls_table)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.back_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def load_hall_statistics(self):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="CinemaBASAA"
            )
            cursor = db.cursor()
            cursor.callproc("CalculateHall")
            self.halls_table.setRowCount(0)

            for result in cursor.stored_results():
                for row_data in result.fetchall():
                    row = self.halls_table.rowCount()
                    self.halls_table.insertRow(row)
                    for column, data in enumerate(row_data):
                        self.halls_table.setItem(row, column, QTableWidgetItem(str(data)))
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные залов: {e}")



class CinemaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кинотеатр - Бронирование билетов")
        self.setFixedSize(800, 600)
        self.initUI()
        self.db = self.connect_to_db()
        if self.db:
            self.cursor = self.db.cursor()
            self.load_movies()

    def initUI(self):
        # Установка шрифта
        font = QFont("Montserrat", 12)

        # Элементы интерфейса
        self.movie_label = QLabel("Выберите фильм:")
        self.movie_label.setFont(font)
        self.movie_label.setStyleSheet("color: #6F4E37;")

        self.movie_combo = QComboBox()
        self.movie_combo.setFont(font)
        self.movie_combo.setStyleSheet("border: 2px solid #A0522D; border-radius: 10px; padding: 5px;")
        self.movie_combo.currentIndexChanged.connect(self.update_showtimes)

        self.showtime_label = QLabel("Выберите время сеанса:")
        self.showtime_label.setFont(font)
        self.showtime_label.setStyleSheet("color: #6F4E37;")

        self.showtime_combo = QComboBox()
        self.showtime_combo.setFont(font)
        self.showtime_combo.setStyleSheet("border: 2px solid #A0522D; border-radius: 10px; padding: 5px;")
        self.showtime_combo.currentIndexChanged.connect(self.update_seats)

        self.seat_label = QLabel("Выберите место:")
        self.seat_label.setFont(font)
        self.seat_label.setStyleSheet("color: #6F4E37;")

        self.seat_combo = QComboBox()
        self.seat_combo.setFont(font)
        self.seat_combo.setStyleSheet("border: 2px solid #A0522D; border-radius: 10px; padding: 5px;")

        self.book_button = QPushButton("Забронировать")
        self.book_button.setFont(font)
        self.book_button.setStyleSheet("background-color: #8B0000; color: white; border-radius: 10px; padding: 10px; font-weight: bold;")
        self.book_button.clicked.connect(self.book_ticket)

        self.back_button = QPushButton("Назад")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("background-color: #6F4E37; color: white; border-radius: 10px; padding: 10px; font-weight: bold;")
        self.back_button.clicked.connect(self.go_back)

        self.fill_percentage_button = QPushButton("Показать процент заполнения зала")
        self.fill_percentage_button.setFont(font)
        self.fill_percentage_button.setStyleSheet("background-color: #D2691E; color: white; border-radius: 10px; padding: 10px;")
        self.fill_percentage_button.clicked.connect(self.show_fill_percentage)

        self.popular_genre_button = QPushButton("Показать самый популярный жанр")
        self.popular_genre_button.setFont(font)
        self.popular_genre_button.setStyleSheet("background-color: #A0522D; color: white; border-radius: 10px; padding: 10px;")
        self.popular_genre_button.clicked.connect(self.show_popular_genre)

        self.export_chart_button = QPushButton("Экспортировать статистику в Excel и график")
        self.export_chart_button.setFont(font)
        self.export_chart_button.setStyleSheet("background-color: #6F4E37; color: white; border-radius: 10px; padding: 10px;")
        self.export_chart_button.clicked.connect(self.export_statistics)

        self.result_display = QTextEdit()
        self.result_display.setFont(font)
        self.result_display.setStyleSheet("border: 2px solid #8B4513; border-radius: 10px; padding: 5px; background-color: #FFF8DC;")
        self.result_display.setReadOnly(True)

        self.info_label = QLabel("")
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("color: #6F4E37; font-weight: bold; font-size: 14px;")

        layout = QVBoxLayout()
        layout.addWidget(self.movie_label)
        layout.addWidget(self.movie_combo)
        layout.addWidget(self.showtime_label)
        layout.addWidget(self.showtime_combo)
        layout.addWidget(self.seat_label)
        layout.addWidget(self.seat_combo)
        layout.addWidget(self.book_button)
        layout.addWidget(self.back_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.result_display)

        procedures_layout = QHBoxLayout()
        procedures_layout.addWidget(self.fill_percentage_button)
        procedures_layout.addWidget(self.popular_genre_button)
        layout.addLayout(procedures_layout)
        layout.addWidget(self.export_chart_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def go_back(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()
    def connect_to_db(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="CinemaBASAA"
            )
        except mysql.connector.Error as e:
            self.info_label.setText(f"Ошибка подключения к базе данных: {e}")

    def load_movies(self):
        try:
            self.cursor.execute("SELECT MovieID, Title, Genre FROM Movie")
            movies = self.cursor.fetchall()
            self.movie_combo.clear()
            for movie in movies:
                self.movie_combo.addItem(f"{movie[1]} ({movie[2]})", movie[0])
        except mysql.connector.Error as err:
            self.info_label.setText(f"Не удалось загрузить фильмы: {err}")

    def update_showtimes(self):
        movie_id = self.movie_combo.currentData()
        if movie_id:
            try:
                self.cursor.execute("""
                    SELECT DISTINCT ShowTime
                    FROM Sessions
                    WHERE MovieID = %s
                """, (movie_id,))
                showtimes = self.cursor.fetchall()
                self.showtime_combo.clear()
                for showtime in showtimes:
                    self.showtime_combo.addItem(str(showtime[0]))
            except mysql.connector.Error as err:
                self.info_label.setText(f"Не удалось загрузить время сеансов: {err}")

    def update_seats(self):
        movie_id = self.movie_combo.currentData()
        showtime = self.showtime_combo.currentText()
        if movie_id and showtime:
            try:
                self.cursor.execute("""
                    SELECT HallID
                    FROM Sessions
                    WHERE MovieID = %s AND ShowTime = %s
                    LIMIT 1
                """, (movie_id, showtime))
                hall = self.cursor.fetchone()
                if hall:
                    self.cursor.execute("SELECT Capacity FROM Hall WHERE HallID = %s", (hall[0],))
                    capacity = self.cursor.fetchone()[0]

                    self.cursor.execute("""
                        SELECT SeatNumber
                        FROM Sale
                        WHERE MovieID = %s AND ShowTime = %s
                    """, (movie_id, showtime))
                    booked_seats = [seat[0] for seat in self.cursor.fetchall()]

                    self.seat_combo.clear()
                    for seat in range(1, capacity + 1):
                        if seat not in booked_seats:
                            self.seat_combo.addItem(str(seat))
            except mysql.connector.Error as err:
                self.info_label.setText(f"Не удалось загрузить места: {err}")

    def book_ticket(self):
        movie_id = self.movie_combo.currentData()
        showtime = self.showtime_combo.currentText()
        seat_number = self.seat_combo.currentText()

        if not (movie_id and showtime and seat_number):
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText("Необходимо выбрать все параметры.")
            return

        try:
            # Получение HallID из таблицы Sessions
            self.cursor.execute("""
                SELECT HallID 
                FROM Sessions 
                WHERE MovieID = %s AND ShowTime = %s
                LIMIT 1
            """, (movie_id, showtime))
            hall_id = self.cursor.fetchone()[0]

            # Добавление записи в таблицу Sale
            self.cursor.execute("""
                INSERT INTO Sale (MovieID, HallID, ShowTime, SeatNumber)
                VALUES (%s, %s, %s, %s)
            """, (movie_id, hall_id, showtime, seat_number))
            self.db.commit()

            # Сообщение об успешном бронировании
            self.info_label.setStyleSheet("color: #228B22;")
            self.info_label.setText(f"Билет успешно забронирован! Зал: {hall_id}")
            self.update_seats()
        except mysql.connector.Error as err:
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText(f"Не удалось забронировать билет: {err}")

    def show_fill_percentage(self):
        try:
            self.result_display.clear()
            self.cursor.callproc("CalculateHall")
            for result in self.cursor.stored_results():
                data = result.fetchall()
                self.result_display.append("Процент заполнения зала:")
                for row in data:
                    hall_id, showtime, booked, capacity, percentage = row
                    self.result_display.append(
                        f"Зал {hall_id}, Время: {showtime}, Мест занято: {booked}/{capacity}, Заполнение: {percentage}%")
        except mysql.connector.Error as err:
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText(f"Не удалось получить процент заполнения зала: {err}")

    def show_popular_genre(self):
        try:
            self.result_display.clear()
            self.cursor.callproc("MostPopular")
            for result in self.cursor.stored_results():
                data = result.fetchall()
                self.result_display.append("Самый популярный жанр:")
                for row in data:
                    genre, count = row
                    self.result_display.append(f"Жанр: {genre}, Продано билетов: {count}")
        except mysql.connector.Error as err:
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText(f"Не удалось получить популярный жанр: {err}")

    def export_statistics(self):
        try:
            self.cursor.callproc("CalculateHall")
            data = []
            for result in self.cursor.stored_results():
                data.extend(result.fetchall())

            df = pd.DataFrame(data, columns=["Зал", "Время", "Забронировано", "Вместимость", "Процент заполнения"])

            file_path = "Cinema_Statistics.xlsx"
            df.to_excel(file_path, index=False, engine='openpyxl')

            plt.figure(figsize=(8, 8))
            hall_sums = df.groupby("Зал")["Процент заполнения"].sum()
            plt.pie(hall_sums, labels=[f"Зал {hall}" for hall in hall_sums.index],
                    autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title("Процент заполнения залов")

            chart_path = "Cinema_Statistics_Chart.png"
            plt.savefig(chart_path)

            self.info_label.setStyleSheet("color: #228B22;")
            self.info_label.setText(
                f"Статистика успешно экспортирована в {file_path} и график сохранён как {chart_path}.")
        except mysql.connector.Error as err:
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText(f"Не удалось экспортировать статистику: {err}")
        except Exception as e:
            self.info_label.setStyleSheet("color: #B22222;")
            self.info_label.setText(f"Ошибка при экспорте: {e}")


if __name__ == "__main__":
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()
