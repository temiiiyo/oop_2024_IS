from railCar import RailCar
from trainSorter import TrainSorter

def main():
    sorter = TrainSorter()
    output_file = "result.txt"

    while True:
        print("\n--- Меню ---")
        print("1. Ввести состав с клавиатуры")
        print("2. Загрузить состав из файла")
        print("3. Показать отсортированные составы")
        print("4. Выйти")

        choice = input("Выберите действие: ")
        if choice == '1':
            cars = []
            n = int(input("Введите количество вагонов: "))
            for _ in range(n):
                car_type = input("Введите тип вагона (грузовой/пассажирский): ").strip()
                if not RailCar.validate(car_type):
                    print(f"Неверный тип вагона: {car_type}. Попробуйте снова.")
                    continue
                cars.append(RailCar(car_type))
            sorter.sort_train(cars)
        elif choice == '2':
            file_name = input("Введите имя файла: ")
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    cars = []
                    for line in file:
                        line = line.strip()
                        if RailCar.validate(line):
                            cars.append(RailCar(line))
                        else:
                            print(f"Неверный тип вагона в файле: {line}. Пропущено.")
                    sorter.sort_train(cars)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '3':
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("Результаты сортировки:\n")
                file.write(f"Направление A: {sorter.direction_a}\n")
                file.write(f"Направление B: {sorter.direction_b}\n")
            print(f"Результаты сохранены в файл: {output_file}")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()