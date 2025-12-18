class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, app_id, priority, executor, deadline, date_completed=None, status=None):
        entry = {
            'app_id': app_id,
            'priority': priority,
            'executor': executor,
            'deadline': deadline,
            'date_completed': date_completed,
            'status': status
        }
        self.entries.append(entry)

    def analyze_journal(self):
        for entry in self.entries:
            print(f"ID:{entry['app_id']} | Приоритет заявки:{entry['priority']} | Исполнитель:{entry['executor']} | "
                  f"Дедлайн:{entry['deadline']} | Дата выполнения:{entry['date_completed']} | Статус:{entry['status']}")