from bd import connect_db, execute_query


def create_tables():
    """Создание таблиц базы данных"""
    try:
        # Создаем таблицу тарифов
        execute_query("""
            CREATE TABLE IF NOT EXISTS tariffs (
                tariff_id INTEGER PRIMARY KEY AUTOINCREMENT,
                price DECIMAL(10, 2) NOT NULL,
                description VARCHAR(255)
            );
        """)

        # Создаем таблицу городов
        execute_query("""
            CREATE TABLE IF NOT EXISTS cities (
                city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                distance INTEGER NOT NULL,
                tariff_id INTEGER,
                FOREIGN KEY (tariff_id) REFERENCES tariffs(tariff_id)
            );
        """)

        # Создаем таблицу звонков
        execute_query("""
            CREATE TABLE IF NOT EXISTS calls (
                call_id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_id INTEGER,
                start_time TIMESTAMP NOT NULL,
                duration INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (city_id) REFERENCES cities(city_id)
            );
        """)

        print("Таблицы созданы успешно.")

    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")


def add_test_data():
    """Добавление тестовых данных"""
    try:
        # Проверяем, есть ли уже данные
        from bd import fetch_data
        tariffs_count = fetch_data("SELECT COUNT(*) FROM tariffs;")[0][0]

        if tariffs_count == 0:
            # Добавляем тарифы
            tariffs = [
                (10.50, 'Базовый тариф'),
                (15.75, 'Повышенный тариф'),
                (8.25, 'Экономичный тариф'),
                (20.00, 'Премиум тариф')
            ]

            for price, description in tariffs:
                execute_query("INSERT INTO tariffs (price, description) VALUES (?, ?);", (price, description))

            # Добавляем города
            cities = [
                ('Москва', 100, 1),
                ('Санкт-Петербург', 200, 2),
                ('Новосибирск', 500, 3),
                ('Екатеринбург', 300, 4),
                ('Казань', 150, 1),
                ('Нижний Новгород', 250, 2)
            ]

            for name, distance, tariff_id in cities:
                execute_query("INSERT INTO cities (name, distance, tariff_id) VALUES (?, ?, ?);",
                              (name, distance, tariff_id))

            # Добавляем тестовые звонки
            calls = [
                (1, '2024-01-15 08:30:00', 15),
                (2, '2024-01-15 09:45:00', 25),
                (3, '2024-01-15 11:20:00', 10),
                (4, '2024-01-15 14:15:00', 30),
                (1, '2024-01-15 16:40:00', 20),
                (5, '2024-01-16 10:00:00', 18),
                (6, '2024-01-16 12:30:00', 22),
                (2, '2024-01-16 15:45:00', 12)
            ]

            for city_id, start_time, duration in calls:
                execute_query("INSERT INTO calls (city_id, start_time, duration) VALUES (?, ?, ?);",
                              (city_id, start_time, duration))

            print("Тестовые данные добавлены успешно.")
        else:
            print("Данные уже существуют.")

    except Exception as e:
        print(f"Ошибка при добавлении тестовых данных: {e}")


if __name__ == "__main__":
    print("Инициализация базы данных...")
    create_tables()
    add_test_data()
    print("База данных готова к использованию!")