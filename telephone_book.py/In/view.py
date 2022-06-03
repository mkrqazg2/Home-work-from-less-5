def new_number():
    value = input ("Введите номер: ")
    word = input ("Введите имя: ")
    dict[word] = value
    print("Контакт добавлен")
    return (value,word)