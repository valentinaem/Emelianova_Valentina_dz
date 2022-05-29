# Задание 3

# Написать функцию thesaurus(),
# принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*workers):
    workers_data = dict()
    for name in workers:
        letter = name[0]
        workers_data.setdefault(letter, [])
        workers_data[letter].append(name)
    return workers_data

print(thesaurus('Kate', 'Kris', 'Nik'))

# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:


def thesaurus_adv(*workers):
    workers_data = dict()
    workers_names = dict()
    for name in workers:
        person = name.split(' ')
        lastname = person[0]
        letter_1 = lastname[0]
        firstname = person[1]
        letter_2 = firstname[0]
        workers_data.setdefault(letter_2, {})
        workers_data[letter_2].setdefault(letter_1, [])
        workers_data[letter_2][letter_1].append(name) # возник вопрос:
        # если словарь в словаре, то чтобы вызвать внутренний словарь нужно писать: workers_data[ключ1][ключ2].append(name)?
        # почему нельзя добавить имя только в оснойной словарь: workers_data[ключ1].append(name)?
        # или почему нельзя доавить сначала в один, потом во второй:
        # workers_data[ключ1].append(name)
        # workers_data[ключ2].append(name)?
    return workers_data
print(thesaurus_adv('Kate Nyx', 'Max Nikson', 'Mike Nale', 'Kris Fox'))