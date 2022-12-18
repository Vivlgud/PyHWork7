import csv
# from datetime import datetime as dt # пока нет!!!
 
def write_data(data, sep=None):
    """Запись данных в файл phone.csv"""
    with open('phone.csv', 'a+', encoding='utf-8') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")

def read_data():
    """Чтение данных из файла phone.csv"""
    with open('phone.csv', 'r', encoding='utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data