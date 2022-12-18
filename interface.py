from import_export import* 
from controller import*
from function import print_data
from search import search_data



def select_operation():
    """Интерфейс пользователя телефонного справочника"""
    
    while True:

        print('''\nКоманды выбора меню:
        Добавить контакт - 1
        Просмотр всех записей - 2
        Поиск контакта - 3
        Выход - 0 \n''')

        menu_selection = input('Введите номер меню: > ')

        if menu_selection == '1':
            list_add=input_data()
            write_data(list_add,sep=", ")        
        elif menu_selection == '2':
            data = read_data()
            print_data(data)
        elif menu_selection == '3':
            word = input("Введите фамилию для поиска: ")
            word=word.upper()
            data = read_data()
            item = search_data(word, data)
            if item != None:
                print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Год рождения".center(15), "Телефон".center(15), "Комментарий".center(20), "Дата и Время внесения".center(20))
                print("-"*130)
                print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
            else:
                print("Данные не обнаружены")
        elif menu_selection == '0':
            print("Работа завершена")
            raise SystemExit
