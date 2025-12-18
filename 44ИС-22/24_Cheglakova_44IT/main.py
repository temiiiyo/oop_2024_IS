from user import User
from application import Application
from journal import Journal

def load_users(filename):
    users = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                user_id, name, role = line.strip().split(',')
                users[int(user_id)] = User(int(user_id), name, role)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    return users

def load_applications(filename, users):
    applications = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                app_id, user_id, app_type = line.strip().split(',')
                user = users[int(user_id)]
                applications.append(Application(int(app_id), user, app_type))
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    return applications

def load_journal(filename):
    journal = Journal()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                app_id, priority, executor, deadline, date_completed, status = line.strip().split(',')
                journal.add_entry(
                    int(app_id),
                    int(priority),
                    executor,
                    deadline,
                    date_completed if date_completed else None,
                    status if status else None
                )
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    return journal

def analyze_applications(applications):
    app_types_count = {}
    total_applications = len(applications)

    for app in applications:
        app_type = app.app_type
        if app_type not in app_types_count:
            app_types_count[app_type] = 0
        app_types_count[app_type] += 1

    return app_types_count, total_applications

def write_otchet(filename, ratios):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Процентное соотношение заявок по типам:\n")
        for app_type, count in ratios.items():
            percent = (count / total_applications) * 100
            f.write(f"{app_type}: {count} ({percent:.2f}%)\n")

if __name__ == "__main__":
    users = load_users('users.txt')
    applications = load_applications('applications.txt', users)
    journal = load_journal('journal.txt')

    app_types_count, total_applications = analyze_applications(applications)
    write_otchet('otchet.txt', app_types_count)

    # Используем метод analyze_journal
    journal.analyze_journal()