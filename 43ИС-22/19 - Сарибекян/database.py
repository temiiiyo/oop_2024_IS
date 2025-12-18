import sqlite3

class Database:
    def __init__(self, db_name='service_requests.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS applicants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            applicant_id INTEGER,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'ожидает',
            executor TEXT,
            repair TEXT,
            created_date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (applicant_id) REFERENCES applicants(id)
        )''')
        self.conn.commit()

    def add_applicant(self, name, contact_info):
        self.cursor.execute("INSERT INTO applicants (name, contact_info) VALUES (?, ?)",
                           (name, contact_info))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_request(self, applicant_id, description, status='ожидает', executor=None, repair=None):
        self.cursor.execute("""
            INSERT INTO requests (applicant_id, description, status, executor, repair) 
            VALUES (?, ?, ?, ?, ?)
        """, (applicant_id, description, status, executor, repair))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_unprocessed_requests(self):
        self.cursor.execute("""
            SELECT r.id, a.name, r.description, r.status, r.executor, r.repair
            FROM requests r
            JOIN applicants a ON r.applicant_id = a.id
            WHERE r.status = 'ожидает'
        """)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()