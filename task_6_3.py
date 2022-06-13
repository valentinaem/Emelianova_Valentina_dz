#  Есть два файла: в одном хранятся ФИО пользователей сайта,
#  а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
#  одна строка — один пользователь, разделитель между значениями — запятая.
#  Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
#  ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
#  Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
#  чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
#  При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
from itertools import zip_longest
import json
users_hobbies = {}
with open('users.csv', 'r', encoding='utf-8') as users, open('hobby.csv', 'r', encoding='utf-8') as hobbies:
    num_lines_users = sum(1 for line in users)
    num_lines_hobbies = sum(1 for line in hobbies)
    if num_lines_users < num_lines_hobbies:
        exit(1)
    users.seek(0)
    hobbies.seek(0)
    for user, hobby in zip_longest(users, hobbies):
        users_hobbies[user.strip()] = hobby.strip() if hobby is not None else hobby
with open('task6_3.json', 'w', encoding='utf-8') as f:
    json.dump(users_hobbies, f, ensure_ascii=False)
print(users_hobbies)