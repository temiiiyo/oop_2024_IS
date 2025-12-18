import psycopg2

# Подключение к базе данных PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="recommendation",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        raise Exception(f"Ошибка подключения к базе данных: {e}")

# Получение данных о расходах за определенный месяц
def get_expenses(conn, start_date, end_date):
    query = """
    SELECT e.date, e.quantity, e.price, ci.name AS cost_item, c.category_name
    FROM "OOOP".expense e
    JOIN "OOOP".categories c ON e.id_categories = c.id
    JOIN "OOOP".cost_item ci ON c.id_cost_item = ci.id
    WHERE e.date BETWEEN %s AND %s;
    """
    cur = conn.cursor()
    cur.execute(query, (start_date, end_date))
    rows = cur.fetchall()
    cur.close()
    return rows

# Получение списка категорий для добавления траты
def get_categories(conn):
    query = "SELECT id, category_name FROM \"OOOP\".categories"
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows