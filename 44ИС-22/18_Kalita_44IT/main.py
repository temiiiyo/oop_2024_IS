from place import Place
from carriage import Carriage
from diesel_locomotive import Locomotive
from composition import Train

if __name__ == '__main__':
    # Создание тепловоза
    locomotive = Locomotive("TEP70", 3000)

    # Создание состава
    train = Train(locomotive)

    # Добавление вагонов
    train.add_carriage(Carriage(1, "Пассажирский"))
    train.add_carriage(Carriage(2, "Пассажирский"))
    train.add_carriage(Carriage(3, "Бистро"))

    # Вывод информации о составе
    print("Исходный состав:")
    print(train)

    # Сохранение состояния состава в файл
    train.save_to_file('tr_data.txt')

    # Загрузка состава из файла
    loaded_train = Train.load_from_file('train_data.txt')
    print("\nЗагруженный состав:")
    print(loaded_train)