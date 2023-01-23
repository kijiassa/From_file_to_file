def ID_list (zz):
    # Задаёт начальный список и ввод нового значения для сравнения
    new_list = []

#открывает файл, читает его и выводит содержимое в виде списка из строк, построчное чтение, файл закрывается
    with open('tumbd.txt','r+') as f:
        s = f.readlines()
        print (s)

#проходит по элементам списка, обрезает \n и перевод в int, добавляет элементы в новый, ранее созданный список
        for x in s:
            x_res = int(x[:12])
            new_list.append(x_res)
            print (x_res)
    print(new_list)

# Проходит по новому списку и смотрит, нет ли в нём нового значения, если нет, то добавляет в список
    if zz not in new_list:
        new_list.append(zz)

    print (new_list)
    print(len(new_list))
# Переводит список в строку, и разделяет, чтобы каждый элемент на новой строчке

    delim = '\n'
    ww = delim.join(map(str,new_list))

# Заново открывает файл и записывает в него новую строку
    with open('tumbd.txt','w') as f:
        f.write(ww)

b = int(input("input IDE"))
ID_list(b)