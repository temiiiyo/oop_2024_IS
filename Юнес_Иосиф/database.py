import sqlite3
import os

# Конфигурация базы данных
DB_NAME = 'telephone_station.db'


def create_database():
    """Создание базы данных и таблиц, если они не существуют"""
    try:
        # Подключаемся к базе данных (файл будет создан автоматически)
        conn = get_connection()
        cursor = conn.cursor()

        # Создаем таблицу тарифов
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tariffs (
                tariff_id INTEGER PRIMARY KEY AUTOINCREMENT,
                price DECIMAL(10, 2) NOT NULL,
                description VARCHAR(255)
            );
        """)

        # Создаем таблицу городов
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cities (
                city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                distance INTEGER NOT NULL,
                tariff_id INTEGER,
                FOREIGN KEY (tariff_id) REFERENCES tariffs(tariff_id)
            );
        """)

        # Создаем таблицу звонков
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calls (
                call_id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_id INTEGER,
                start_time TIMESTAMP NOT NULL,
                duration INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (city_id) REFERENCES cities(city_id)
            );
        """)

        conn.commit()
        print("Таблицы созданы успешно.")

        # Добавляем тестовые данные, если таблицы пустые
        add_test_data(cursor, conn)

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")


def add_test_data(cursor, conn):
    """Добавление тестовых данных"""
    try:
        # Проверяем, есть ли уже данные в таблице тарифов
        cursor.execute("SELECT COUNT(*) FROM tariffs;")
        if cursor.fetchone()[0] == 0:
            # Добавляем тарифы
            tariffs = [
                (10.50, 'Базовый тариф'),
                (15.75, 'Повышенный тариф'),
                (8.25, 'Экономичный тариф'),
                (20.00, 'Премиум тариф')
            ]

            cursor.executemany("""
                INSERT INTO tariffs (price, description) 
                VALUES (?, ?);
            """, tariffs)

            # Получаем ID добавленных тарифов
            cursor.execute("SELECT tariff_id FROM tariffs ORDER BY tariff_id;")
            tariff_ids = [row[0] for row in cursor.fetchall()]

            # Добавляем города
            cities = [
                ('Москва', 100, tariff_ids[0]),
                ('Санкт-Петербург', 200, tariff_ids[1]),
                ('Новосибирск', 500, tariff_ids[2]),
                ('Екатеринбург', 300, tariff_ids[3]),
                ('Казань', 150, tariff_ids[0]),
                ('Нижний Новгород', 250, tariff_ids[1])
            ]

            cursor.executemany("""
                INSERT INTO cities (name, distance, tariff_id) 
                VALUES (?, ?, ?);
            """, cities)

            # Получаем ID добавленных городов
            cursor.execute("SELECT city_id FROM cities ORDER BY city_id;")
            city_ids = [row[0] for row in cursor.fetchall()]

            # Добавляем тестовые звонки
            calls = [
                (city_ids[0], '2024-01-15 08:30:00', 15),
                (city_ids[1], '2024-01-15 09:45:00', 25),
                (city_ids[2], '2024-01-15 11:20:00', 10),
                (city_ids[3], '2024-01-15 14:15:00', 30),
                (city_ids[0], '2024-01-15 16:40:00', 20),
                (city_ids[4], '2024-01-16 10:00:00', 18),
                (city_ids[5], '2024-01-16 12:30:00', 22),
                (city_ids[1], '2024-01-16 15:45:00', 12)
            ]

            cursor.executemany("""
                INSERT INTO calls (city_id, start_time, duration) 
                VALUES (?, ?, ?);
            """, calls)

            conn.commit()
            print("Тестовые данные добавлены успешно.")

    except Exception as e:
        print(f"Ошибка при добавлении тестовых данных: {e}")
        conn.rollback()


def get_connection():
    """Создание подключения к базе данных SQLite"""
    try:
        conn = sqlite3.connect(DB_NAME)
        # Включаем поддержку внешних ключей
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise


def execute_query(query, params=None, fetch=False):
    """
    Выполнение SQL-запроса

    Args:
        query: SQL-запрос
        params: Параметры для запроса (кортеж)
        fetch: Если True, возвращает результат запроса
    """
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch:
            result = cursor.fetchall()
        else:
            result = None

        conn.commit()
        return result if fetch else True

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        if conn:
            conn.rollback()
        return False if not fetch else None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_data(query, params=None):
    """
    Получение данных из базы данных

    Args:
        query: SQL-запрос
        params: Параметры для запроса (кортеж)
    """
    return execute_query(query, params, fetch=True)


def init_database():
    """Инициализация базы данных (создание таблиц и тестовых данных)"""
    create_database()


def clear_database():
    """Очистка всех данных из таблиц (для тестирования)"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Удаляем данные в правильном порядке (с учетом внешних ключей)
        cursor.execute("DELETE FROM calls;")
        cursor.execute("DELETE FROM cities;")
        cursor.execute("DELETE FROM tariffs;")

        # Сбрасываем автоинкрементные счетчики
        cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('calls', 'cities', 'tariffs');")

        conn.commit()
        cursor.close()
        conn.close()

        print("База данных очищена.")

    except Exception as e:
        print(f"Ошибка при очистке базы данных: {e}")


# Функции для работы с конкретными таблицами
def get_all_cities():
    """Получение списка всех городов"""
    query = "SELECT city_id, name, distance FROM cities ORDER BY name;"
    return fetch_data(query)


def get_all_tariffs():
    """Получение списка всех тарифов"""
    query = "SELECT tariff_id, price, description FROM tariffs ORDER BY price;"
    return fetch_data(query)


def get_calls_by_date(start_date, end_date):
    """
    Получение звонков за период

    Args:
        start_date: Начальная дата (строка в формате 'YYYY-MM-DD')
        end_date: Конечная дата (строка в формате 'YYYY-MM-DD')
    """
    query = """
        SELECT c.call_id, ci.name, c.start_time, c.duration, t.price
        FROM calls c
        JOIN cities ci ON c.city_id = ci.city_id
        JOIN tariffs t ON ci.tariff_id = t.tariff_id
        WHERE DATE(c.start_time) BETWEEN ? AND ?
        ORDER BY c.start_time;
    """
    return fetch_data(query, (start_date, end_date))


def get_city_statistics():
    """Получение статистики по городам"""
    query = """
        SELECT 
            ci.name,
            COUNT(c.call_id) as total_calls,
            SUM(c.duration) as total_duration,
            SUM(c.duration * t.price) as total_cost
        FROM cities ci
        LEFT JOIN calls c ON ci.city_id = c.city_id
        JOIN tariffs t ON ci.tariff_id = t.tariff_id
        GROUP BY ci.city_id, ci.name
        ORDER BY total_cost DESC;
    """
    return fetch_data(query)


if __name__ == "__main__":
    # Инициализация базы данных при прямом запуске файла
    init_database()
    print("База данных инициализирована.")