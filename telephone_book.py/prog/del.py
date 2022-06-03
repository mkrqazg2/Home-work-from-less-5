#def delete():
# dict = []
# #word = input("Введите контакт,который нужно удалить: ")

# with open("dict.txt", "r") as f:
#     dict = f.readlines()
#     #with open("dict.txt", "w+") as f:
#         #dict.remove(word)

#     #for line in dict:
#         #if line != word:
#             #f.write(line)

# #     lines = f.readlines()
# # with open("dict.txt", "w") as f:
# #     for line in lines:
# #         if line.strip("\n") != 'word':
# #             f.write(line)
#     #print("контакт", word, " удалён")
# print(dict)
import re

word = input("Введите контакт,который нужно удалить: ")
with open('dict.txt') as f:
    lines = f.readlines()
str = 'word'
pattern = re.compile(re.escape(str))
with open('dict.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)


        