# def ad_contact(dict):
#     with open('dict_1.txt','a') as f:
#         f.write(dict,'\n')


dict ={
   "Андрей" : '123',
   "Борис" : "456",
   "Виктор" : "789"}
print("="*15, "Телефонная книга", "="*15)

help_message = """
s - поиск контакта
a - добавить новый контакт
r - удалить контакт
d - вывод всей книги
h - справка
q - выход
"""
choice = ""
while choice != "q":
    choice = input("<< (h - справка) >> Введите команду:  ")
    if choice == "s":
        word = input ("Введите имя: ")
        res = dict.get (word, "Контакта с таким именем нет")
        print(res)
    elif choice == "a":
        value = input ("Введите номер: ")
        word = input ("Введите имя: ")
        dict[word] = value
        print("Контакт добавлен")
    elif choice == "r":
        word = input("Введите контакт,который нужно удалить: ")
        del dict[word]
        print("контакт", word, " удалён")
    elif choice == "d":
        for word in dict:
            print(word, ": ", dict[word])
    elif choice == "h":
        print(help_message)
    elif choice == "q":
        print('книга закрыта')
        continue;
    else:
        print("недопустимая команда. Введите h для справки")