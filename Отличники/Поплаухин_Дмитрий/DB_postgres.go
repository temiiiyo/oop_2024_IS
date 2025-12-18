package test

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq" // Импортируем драйвер PostgreSQL
)

type Category struct {
	Code int
	Name string
}

type Room struct {
	Code     int
	Category int
	Number   int
	Capacity int
}

type Citizen struct {
	Code     int
	Name     string
	Passport string
}

type Placement struct {
	Code      int
	Citizen   int
	Room      int
	StartDate string
	Duration  int
}

func main() {
	// Параметры подключения к базе данных PostgreSQL
	connStr := "postgres://postgres:postgres@localhost:5433/postgres?sslmode=disable"

	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	if err = db.Ping(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Успешное подключение к базе данных!")

	if _, err = execOnMigration(db); err != nil {
		log.Fatalf("Ошибка миграции: %v", err)
	}

	log.Println("Миграция выполнена успешно")

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

func countFreeRoomsPG(db *sql.DB) (int, error) {
	var count int
	err := db.QueryRow(`
			-- Пример запроса для проверки количества свободных номеров
			SELECT COUNT(r.Код_номера)
			FROM Номера r
			WHERE NOT EXISTS (
	   		SELECT 1
	   		FROM Размещение p
	   		WHERE p.код_номера = r.Код_номера
			);
	       `).Scan(&count)
	return count, err
}

func calculateCategoryOccupancyPG(db *sql.DB) (map[string]float64, error) {
	rows, err := db.Query(`
	       -- Пример запроса для проверки занятости по категориям
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

func execOnMigrationPG(db *sql.DB) (sql.Result, error) {
	migration := `
			drop table Граждане cascade;
			drop table Категории cascade;
			drop table Номера cascade;
			drop table Размещение cascade;

			CREATE TABLE Категории (
	   	Код_категории SERIAL PRIMARY KEY,
	   	название VARCHAR(255)
			);

			CREATE TABLE Номера (
	   		Код_номера SERIAL PRIMARY KEY,
	   		код_категории INTEGER REFERENCES Категории(Код_категории),
	   		номер INTEGER unique,
	   		мест INTEGER
			);

			CREATE TABLE Граждане (
	   		Код_гражданина SERIAL PRIMARY KEY,
	   		ФИО VARCHAR(255),
	   		паспорт VARCHAR(255)
			);

			CREATE TABLE Размещение (
	   		Код_размещения SERIAL PRIMARY KEY,
	   		код_гражданина INTEGER REFERENCES Граждане(Код_гражданина),
	   		код_номера INTEGER REFERENCES Номера(номер),
	   		дата_въезда DATE,
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

	return db.Exec(migration)
}
