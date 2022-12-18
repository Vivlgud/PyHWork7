def print_data(data):
    """Вывод в терминал телефонного справочника"""
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Комментарий".center(20), "Дата и Время внесения".center(20))
        print("-"*130)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
    else:
        print("Справочник пуст!")


def correct_input(text):
    ''' Проверка на корректный ввод букв'''
    name = input(f'{text} > ')
    if name == '*':
        return name 
    while not name.isalpha():
        print('не корректный ввод')
        name = input(f'{text} > ')
    return name.upper()
    
 
def correct_number(text):
    ''' Проверка на корректный ввод номера телефона'''
    number = input(f'{text} > ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input(f'{text} > ')
        
def correct_age(text):
    '''Проверка на корректный ввод года рождения'''
    age = input(f'{text} > ')
    while True:
        if age.isdigit() and len(age) == 4 and (age[:2]=='19' or age[:2]=='20'):
            return age
        print('введите правильный год')
        age = input(f'{text} > ')
    
        
