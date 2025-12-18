package main

import (
    "log"
    "fmt"

    "github.com/jmoiron/sqlx"
    "github.com/xuri/excelize/v2"
    "time"

    _ "github.com/go-sql-driver/mysql"
)

type Hall struct {
    ID       int `db:"hall_id"`
    Capacity int `db:"capacity"`
}

type Movie struct {
    ID    int    `db:"movie_id"`
    Title string `db:"title"`
    Genre string `db:"genre"`
}

type Sale struct {
    ID         int       `db:"sale_id"`
    MovieID    int       `db:"movie_id"`
    HallID     int       `db:"hall_id"`
    ShowTime   time.Time `db:"show_time"`
    SeatNumber int       `db:"seat_number"`
}

type Database struct {
    *sqlx.DB
}

func (db *Database) GetHallOccupancy() (map[int]float64, error) {
    occupancy := make(map[int]float64)

    rows, err := db.Queryx(`
        SELECT s.hall_id,
               COUNT(s.seat_number) AS occupied_seats,
               h.capacity
        FROM Sale s
        JOIN Hall h ON s.hall_id = h.hall_id
        GROUP BY s.hall_id, h.capacity
    `)
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    for rows.Next() {
        var hallID, occupiedSeats, capacity int
        if err := rows.Scan(&hallID, &occupiedSeats, &capacity); err != nil {
            return nil, err
        }
        if capacity > 0 {
            occupancy[hallID] = float64(occupiedSeats) / float64(capacity) * 100
        }
    }
    return occupancy, nil
}

func (db *Database) GetMostPopularGenre() (string, error) {
    var movieID int
    var genre string

    // получаем ID самого популярного фильма
    err := db.Get(&movieID, `
        SELECT movie_id
        FROM Sale
        GROUP BY movie_id
        ORDER BY COUNT(*) DESC
        LIMIT 1
    `)
    if err != nil {
        return "", err
    }

    // получаем жанр этого фильма
    err = db.Get(&genre, `
        SELECT genre
        FROM Movie
        WHERE movie_id = ?
    `, movieID)

    return genre, err
}

func ExportToExcel(occupancy map[int]float64, popularGenre string) error {
    f := excelize.NewFile()
    sheet := "Sheet1"

    // Заголовки
    f.SetCellValue(sheet, "A1", "ID Зала")
    f.SetCellValue(sheet, "B1", "Процент Наполнения")
    f.SetCellValue(sheet, "C1", "Самый Популярный Жанр")

    row := 2
    for hallID, percent := range occupancy {
        f.SetCellValue(sheet, fmt.Sprintf("A%d", row), hallID)
        f.SetCellValue(sheet, fmt.Sprintf("B%d", row), percent)
        f.SetCellValue(sheet, fmt.Sprintf("C%d", row), popularGenre)
        row++
    }

    if err := f.SaveAs("cinema_report.xlsx"); err != nil {
        return err
    }
    return nil
}

func main() {
    dsn := "root:root@tcp(localhost:3306)/cinema"
    db, err := sqlx.Connect("mysql", dsn)
    if err != nil {
        log.Fatalln(err)
    }
    database := &Database{db}

    occupancy, err := database.GetHallOccupancy()
    if err != nil {
        log.Fatalln("Ошибка получения заполненности залов:", err)
    }

    popularGenre, err := database.GetMostPopularGenre()
    if err != nil {
        log.Fatalln("Ошибка получения самого популярного жанра:", err)
    }

    if err := ExportToExcel(occupancy, popularGenre); err != nil {
        log.Fatalln("Ошибка экспорта в Excel:", err)
    }

    log.Println("Отчет успешно создан: cinema_report.xlsx")
}