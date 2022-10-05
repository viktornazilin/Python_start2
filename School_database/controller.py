from push_data import *
from read_data import *
from print_data import *
from search_data import *


def greeting():
    print("Здравствуйте!")

def start():
    print("Выберите опцию:\n\
    1 - Получить всю информацию об учениках;\n\
    2 - Добавить ученика;\n\
    3 - Поиск ученика;\n\
    4 - Выход.")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        elif ch == '4':
            print("Сеанс окончен, до свидания")
            break
        else:
            print("Введите корректную цифру")
            start()