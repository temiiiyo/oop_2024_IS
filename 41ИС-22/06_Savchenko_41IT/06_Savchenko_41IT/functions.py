from Nakladnaya_class import Nakladnaya
import datetime
import openpyxl


def add_nacl(it_list):
    print('Создание накладной')
    rec = input('Введите получателя: ')

    for i in it_list:
        print(i.item_id)

    items_id = list(map(int, input('Введите id товаров для добавления в накладную: ').split()))

    items_to_nacl = {x: int(input(f'Введите количество товара №{x.item_id}: ')) for x in it_list if x.item_id in items_id}

    nacl = Nakladnaya(date=datetime.date.today(), receiver=rec, items=items_to_nacl)
    return nacl


def edit_nacl():
    global nacl_list, items_list
    print('Редактирование накладной')
    rec = input('Введите получателя: ')

    nacl_for_edit = None

    for i in nacl_list:
        if i.receiver == rec:
            nacl_for_edit = i

    nacl_index = nacl_list.index(nacl_for_edit)

    rec = input('Введите нового получателя: ')
    date = input('Введите новую дату: ')

    nacl_list[nacl_index].receiver = rec
    nacl_list[nacl_index].date = date

    return


def nacl_to_excel(nacl: Nakladnaya):
    try:
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = f'{str(nacl.date)}'
        sheet.append(['Товар', 'Количество'])

        for item, amount in nacl.items.items():
            sheet.append([item.name, str(amount)])

        file_path = f'{nacl.receiver}.xlsx'
        wb.save(file_path)
        print(f'Накладная экспортирована в файл {file_path}')
    except Exception as e:
        print(e)