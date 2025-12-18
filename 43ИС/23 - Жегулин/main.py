import pymysql as mds
from customer import Customer
from product import Product
from warranty_claim import WarrantyClaim
from repair import Repair
from replacement import Replacement
from repair_master import RepairMaster


def create_database_if_not_exists():
    """Создает базу данных и таблицы если их не существует"""
    try:
        # Пробуем подключиться без указания базы данных
        connection = mds.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = connection.cursor()

        # Создаем базу данных если её нет
        cursor.execute("CREATE DATABASE IF NOT EXISTS warranty_system")
        cursor.execute("USE warranty_system")

        # Создаем таблицы если их нет
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                warranty_period INT NOT NULL
            )
        """)

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
        print("База данных и таблицы проверены/созданы успешно!")
        return True

    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")
        return False

def connect_to_db():
    return mds.connect(
        host="localhost",
        user="root",
        password="root",
        database="warranty_system"
    )


def read_data_from_file(filename="in.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().strip().split(',')
        return data


def insert_customer(customer):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO customers (name, email) 
        VALUES (%s, %s)
    """, (customer.name, customer.email))
    db_connection.commit()
    customer.id = cursor.lastrowid
    db_connection.close()
    print(f"Клиент {customer.name} добавлен в базу данных.")


def insert_product(product):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO products (name, price, warranty_period) 
        VALUES (%s, %s, %s)
    """, (product.name, product.price, product.warranty_period))
    db_connection.commit()
    product.id = cursor.lastrowid
    db_connection.close()
    print(f"Продукт {product.name} добавлен в базу данных.")


def insert_warranty_claim(warranty_claim):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO warranty_claims (customer_id, product_id, date, reason, status, decision) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (warranty_claim.customer.id, warranty_claim.product.id, warranty_claim.date, warranty_claim.reason, warranty_claim.status, warranty_claim.decision))
    db_connection.commit()
    warranty_claim.id = cursor.lastrowid
    db_connection.close()
    print(f"Гарантийная заявка {warranty_claim.id} добавлена в базу данных.")


def insert_repair(repair):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO repairs (warranty_claim_id, repair_cost, repair_date, description) 
        VALUES (%s, %s, %s, %s)
    """, (repair.warranty_claim.id, repair.repair_cost, repair.repair_date, repair.description))
    db_connection.commit()
    repair.id = cursor.lastrowid
    db_connection.close()
    print(f"Ремонт {repair.id} добавлен в базу данных.")


def insert_replacement(replacement):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO replacements (warranty_claim_id, replacement_date, reason) 
        VALUES (%s, %s, %s)
    """, (replacement.warranty_claim.id, replacement.replacement_date, replacement.reason))
    db_connection.commit()
    replacement.id = cursor.lastrowid
    db_connection.close()
    print(f"Замена {replacement.id} добавлена в базу данных.")


def generate_report():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT wc.id, c.name, p.name, wc.date, wc.reason, wc.status, wc.decision, r.repair_cost, r.repair_date, repl.replacement_date, repl.reason
        FROM warranty_claims wc
        JOIN customers c ON wc.customer_id = c.id
        JOIN products p ON wc.product_id = p.id
        LEFT JOIN repairs r ON wc.id = r.warranty_claim_id
        LEFT JOIN replacements repl ON wc.id = repl.warranty_claim_id
    """)

    claims_data = cursor.fetchall()
    db_connection.close()

    import pandas as pd
    df = pd.DataFrame(claims_data,
                      columns=["ID", "Customer", "Product", "Claim Date", "Reason", "Status", "Decision", "Repair Cost",
                               "Repair Date", "Replacement Date", "Replacement Reason"])

    df['Total Cost'] = df['Repair Cost'].fillna(0) + df['Replacement Date'].apply(
        lambda x: 0 if pd.isna(x) else 100)

    df.to_excel('warranty_report.xlsx', index=False)

    print("Отчет сгенерирован и сохранен в 'warranty_report.xlsx'.")


def main():

    if not create_database_if_not_exists():
        print("Не удалось создать базу данных. Программа остановлена.")
        return

    # Остальной код без изменений:
    data = read_data_from_file()

    customer1 = Customer(1, data[0], data[1])
    insert_customer(customer1)

    data = read_data_from_file()

    customer1 = Customer(1, data[0], data[1])
    insert_customer(customer1)

    product1 = Product(1, data[2], float(data[3]), int(data[4]))
    insert_product(product1)

    claim1 = WarrantyClaim(1, customer1, product1, data[5], data[6], data[7], data[8])
    insert_warranty_claim(claim1)

    RepairMaster(1, data[9], data[10], float(data[11]))
    repair1 = Repair(1, claim1, float(data[11]), data[12], data[13])
    insert_repair(repair1)

    replacement1 = Replacement(1, claim1, data[14], data[15])
    insert_replacement(replacement1)

    repair1.perform_repair()
    repair1.calculate_total_cost(500)

    replacement1.perform_replacement()

    generate_report()

if __name__ == "__main__":
    main()
