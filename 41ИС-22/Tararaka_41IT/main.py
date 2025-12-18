from vizitor import Visitor
from garderob import Garderob
from methods import get_names, return_clothes


def main():
    ploshadka = Garderob()
    with open("visitors.txt", "r") as file:
        for line in file:
            id, name, dress_number = line.replace("\n", '').split(";")
            ploshadka.add(Visitor(int(id), name, int(dress_number)))
    returned_clothes = Garderob()
    while True:
        print("1: Вывести всю очередь\n2: Вывести очередь сдачи одежды\n3: Добавить в обратную очередь\n4: Следующий в очереди на сдачу\n5: Следющий в очереди на получение\nexit: выход")
        func = input("Введите ваш выбор: ")
        if func == '1':
            get_names(ploshadka)
        elif func == '2':
            get_names(returned_clothes)
        elif func == '3':
            id = int(input('Введите id посетителя: '))
            returned_clothes.add(return_clothes(ploshadka, id))
        elif func == '4':
            ploshadka.pop_up()
            try:
                print(ploshadka.head.__getattribute__('name'))
            except Exception:
                print("Очередь пуста")
        elif func == '5':
            returned_clothes.pop_up()
            try:
                print(returned_clothes.head.__getattribute__('name'))
            except Exception:
                print("Очередь пуста")
        elif func == 'exit':
            break


if __name__ == '__main__':
    main()