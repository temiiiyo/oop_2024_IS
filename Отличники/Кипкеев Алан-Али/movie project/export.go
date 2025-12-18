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