package test

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	dbPath := "hotel.db" // Путь к файлу базы данных

	// Проверяем, существует ли файл базы данных
	if _, err := os.Stat(dbPath); os.IsNotExist(err) {
		fmt.Println("Файл базы данных не найден, создаем...")
		// Создаем пустой файл базы данных
		file, err := os.Create(dbPath)
		if err != nil {
			log.Fatalf("Ошибка создания файла базы данных: %v", err)
		}
		file.Close()

		// Открываем соединение с только что созданной базой
		db, err := sql.Open("sqlite3", dbPath)
		if err != nil {
			log.Fatalf("Ошибка открытия базы данных: %v", err)
		}
		defer db.Close()

		// Выполняем миграцию
		if _, err = execOnMigration(db); err != nil {
			log.Fatalf("Ошибка миграции: %v", err)
		}

		log.Println("Миграция выполнена успешно")
	} else if err != nil {
		// Обработка других ошибок os.Stat
		log.Fatalf("Ошибка проверки файла базы данных: %v", err)
	} else {
		fmt.Println("Файл базы данных уже существует, миграция пропущена.")
	}

	// Открываем соединение (если файл уже существовал или был создан)
	db, err := sql.Open("sqlite3", dbPath)
	if err != nil {
		log.Fatalf("Ошибка открытия базы данных: %v", err)
	}
	defer db.Close()

	if err = db.Ping(); err != nil {
		log.Fatalf("Ошибка проверки соединения: %v", err)
	}

	fmt.Println("Успешное подключение к базе данных!")

	// 1. Количество полностью свободных номеров
	freeRoomsCount, err := countFreeRooms(db)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Количество полностью свободных номеров: %d\n", freeRoomsCount)

	// 2. Сравнительная степень занятости номеров по категориям (в процентах)
	categoryOccupancy, err := calculateCategoryOccupancy(db)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Степень занятости номеров по категориям:")
	for category, occupancy := range categoryOccupancy {
		fmt.Printf("Категория '%s': %.2f%%\n", category, occupancy)
	}
}

func countFreeRooms(db *sql.DB) (int, error) {
	var count int
	err := db.QueryRow(`
                SELECT COUNT(Код_номера)
                FROM Номера
                WHERE NOT EXISTS (
                        SELECT 1
                        FROM Размещение
                        WHERE Размещение.код_номера = Номера.Код_номера
                );
        `).Scan(&count)
	return count, err
}

func calculateCategoryOccupancy(db *sql.DB) (map[string]float64, error) {
	rows, err := db.Query(`
                SELECT c.название, COUNT(DISTINCT r.Код_номера) as total_rooms, COUNT(DISTINCT p.код_номера) as occupied_rooms
				FROM Категории c
				LEFT JOIN Номера r
					ON c.Код_категории = r."код_категории"
				LEFT JOIN Размещение p
					ON r.номер = p."код_номера"
				GROUP BY c.название;
        `)

	if err != nil {
		return nil, err
	}
	defer rows.Close()

	categoryOccupancy := make(map[string]float64)
	for rows.Next() {
		var categoryName string
		var totalRooms int
		var occupiedRooms int
		if err := rows.Scan(&categoryName, &totalRooms, &occupiedRooms); err != nil {
			return nil, err
		}

		if totalRooms > 0 {
			occupancy := float64(occupiedRooms) / float64(totalRooms) * 100
			categoryOccupancy[categoryName] = occupancy
		} else {
			categoryOccupancy[categoryName] = 0 // Избегаем деления на ноль
		}
	}

	return categoryOccupancy, nil
}

func execOnMigration(db *sql.DB) (sql.Result, error) {
	migration := `
                CREATE TABLE Категории (
                        Код_категории INTEGER PRIMARY KEY AUTOINCREMENT,
                        название TEXT
                );

                CREATE TABLE Номера (
                        Код_номера INTEGER PRIMARY KEY AUTOINCREMENT,
                        код_категории INTEGER REFERENCES Категории(Код_категории),
                        номер INTEGER UNIQUE,
                        мест INTEGER
                );

                CREATE TABLE Граждане (
                        Код_гражданина INTEGER PRIMARY KEY AUTOINCREMENT,
                        ФИО TEXT,
                        паспорт TEXT
                );

                CREATE TABLE Размещение (
                        Код_размещения INTEGER PRIMARY KEY AUTOINCREMENT,
                        код_гражданина INTEGER REFERENCES Граждане(Код_гражданина),
                        код_номера INTEGER REFERENCES Номера(Код_номера),
                        дата_въезда TEXT,
                        срок_проживания INTEGER
                );

                -- Заполняем таблицу Категории
                INSERT INTO Категории (название) VALUES
                        ('Эконом'),
                        ('Стандарт'),
                        ('Люкс');

                -- Заполняем таблицу Номера
                INSERT INTO Номера (код_категории, номер, мест) VALUES
                (1, 101, 2), -- Эконом
                (1, 102, 1), -- Эконом
                (1, 103, 2), -- Эконом
                (2, 201, 2), -- Стандарт
                (2, 202, 1), -- Стандарт
                (2, 203, 3), -- Стандарт
                (3, 301, 2), -- Люкс
                (3, 302, 1); -- Люкс

                -- Заполняем таблицу Граждане
                INSERT INTO Граждане (ФИО, паспорт) VALUES
                        ('Иванов Иван Иванович', '1234 567890'),
                        ('Петров Петр Петрович', '9876 543210'),
                        ('Сидоров Сидор Сидорович', '1122 334455'),
                        ('Смирнов Алексей Сергеевич', '5544 332211');

                -- Заполняем таблицу Размещение (создаем несколько занятых номеров)
                INSERT INTO Размещение (код_гражданина, код_номера, дата_въезда, срок_проживания) VALUES
                        (1, 101, '2024-01-01', 5), -- Занят номер 101 (Эконом)
                        (2, 201, '2024-01-05', 3), -- Занят номер 201 (Стандарт)
                        (3, 203, '2024-01-10', 7), -- Занят номер 203 (Стандарт)
                        (4, 301, '2024-01-15', 2); -- Занят номер 301 (Люкс)

                -- Дополнительные тестовые данные для проверки граничных случаев

                -- Номер без категории
                INSERT INTO Номера (номер, мест) VALUES (401, 2);

                -- Категория без номеров
                INSERT INTO Категории (название) VALUES ('Суперлюкс');

                -- Заняты все номера в категории
                INSERT INTO Размещение (код_гражданина, код_номера, дата_въезда, срок_проживания) VALUES
                        (1, 102, '2024-02-01', 5), -- Занят номер 102 (Эконом)
                        (2, 103, '2024-02-05', 3); -- Занят номер 103 (Эконом)
        `

	_, err := db.Exec(migration)
	return nil, err
}
