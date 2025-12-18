from wardrobe import Wardrobe
from visitor_builder import VisitorBuilder

def print_menu():
    print("\nМеню:")
    print("1. Загрузить данные из файла")
    print("2. Добавить посетителя")
    print("3. Удалить посетителя")
    print("4. Сохранить данные в файл")
    print("5. Выйти")

def main():
    wardrobe = Wardrobe()

    while True:
        print_menu()
        choice = input("Выберите опцию: ")

        if choice == '1':
            wardrobe.load_from_file('visitors.txt')
            print("Данные загружены из файла.")
        elif choice == '2':
            id = int(input("Введите ID посетителя: "))
            name = input("Введите имя посетителя: ")
            dress_number = int(input("Введите номер одежды: "))
            visitor = (VisitorBuilder()
                       .set_id(id)
                       .set_name(name)
                       .set_dress_number(dress_number)
                       .build())
            wardrobe + visitor
            print("Посетитель добавлен.")
        elif choice == '3':
            visitor = wardrobe.remove_visitor()
            if visitor:
                print(f"Посетитель {visitor.get_name()} удален.")
            else:
                print("Очередь пуста.")
        elif choice == '4':
            wardrobe.save_to_file('wardrobe.txt')
            print("Данные сохранены в файл.")
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()