import pymysql as mds


def create_database_and_tables():
    # 1. Подключаемся к MySQL без указания базы данных
    print("Подключение к MySQL...")
    connection = mds.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = connection.cursor()

    # 2. Создаем базу данных если её нет
    print("Создание базы данных 'warranty_system'...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS warranty_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

    # 3. Используем созданную базу данных
    cursor.execute("USE warranty_system")

    # 4. Создаем таблицы
    print("Создание таблиц...")

    # Таблица клиентов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)

    # Таблица продуктов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            warranty_period INT NOT NULL
        )
    """)

    # Таблица гарантийных заявок
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warranty_claims (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            product_id INT NOT NULL,
            date DATE NOT NULL,
            reason TEXT NOT NULL,
            status VARCHAR(50) NOT NULL,
            decision VARCHAR(50),
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # Таблица ремонтов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repairs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            warranty_claim_id INT NOT NULL,
            repair_cost DECIMAL(10, 2) NOT NULL,
            repair_date DATE NOT NULL,
            description TEXT,
            FOREIGN KEY (warranty_claim_id) REFERENCES warranty_claims(id)
        )
    """)

    # Таблица замен
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS replacements (
            id INT AUTO_INCREMENT PRIMARY KEY,
            warranty_claim_id INT NOT NULL,
            replacement_date DATE NOT NULL,
            reason TEXT,
            FOREIGN KEY (warranty_claim_id) REFERENCES warranty_claims(id)
        )
    """)

    connection.commit()
    connection.close()

    print("=" * 50)
    print("База данных 'warranty_system' и все таблицы успешно созданы!")
    print("=" * 50)


if __name__ == "__main__":
    try:
        create_database_and_tables()
    except Exception as e:
        print(f"Ошибка: {e}")
        print("\nВозможные причины:")
        print("1. MySQL не запущен")
        print("2. Неправильный пароль (у вас указан 'root')")
        print("3. Нет прав у пользователя 'root'")
        print("\nРешение:")
        print("- Запустите службу MySQL")
        print("- Проверьте пароль: mysql -u root -p")