# Программа-словарь, работающая из cmd, позволяющая просматривать, добавлять, удалять, изменять и искать контактные данные.
# А также, сохраняющая адресную книгу на диске для последующего доступа.

import pickle

# имя файла для хранения аддресной книги
cbookfile = 'cbookfile.data'

cbook = {"Sasha": "1111111",
         "Katya": "2222222",
         "Lena": "3333333"}

running = True
while running:
    y = input("Введите s для поиска по аддресной книге, a для добавления контакта, d для удаления и r для изменения: ")
    if y == "s":
        x = input("Введите имя контакта или q для выхода: ")
        if x == "q":
            f = open('cbookfile.data', 'wb')
            pickle.dump(cbook, f)  # помещаем объект в файл
            f.close()
            running = False
            g = open(cbookfile, 'rb')
            storedbook = pickle.load(g)
            print(storedbook)
        elif cbook.__contains__(x) == True:
            print(cbook[x])
        else:
            print("Контакт отсутствует")
    elif y == "a":
        a1 = input("Введите имя контакта: ")
        a2 = input("Введите номер телефона контакта: ")
        cbook[str(a1)] = a2
        print(cbook)
    elif y == "d":
        d1 = input("Введите имя контакта для удаления: ")
        del cbook[str(d1)]
        print(cbook)
    elif y == "r":
        r1 = input("Введите имя контакта, подлежащего замене: ")
        r2 = input("Введите новый номер контакта: ")
        cbook[str(r1)] = r2
    else:
        print("Неизвестная команда")
