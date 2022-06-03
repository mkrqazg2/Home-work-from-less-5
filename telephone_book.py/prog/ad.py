#def ad():
dict = {}
with open('dict.txt','a') as f:  # открытие в режиме запис
    value = input ("Введите номер: ")
    word = input ("Введите имя: ")
    dict.update({word:value})	 # Добавляем в словарь
    dict_ad = str(dict)
    print ('Контакт ' +word+ ' добавлен')

    dict[word] = value
    f.write(dict_ad +'\n')  # запись  в файл
    