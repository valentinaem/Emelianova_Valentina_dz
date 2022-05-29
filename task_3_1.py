# Задание 1.

dictionary = {'zero': 'ноль',
              'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'}


def num_translate(key):
    return dictionary.get(key)

key = input('Введите число от 0 до 10 на английском языке, что бы узнать перевод: ')
print(num_translate(key))

# Задание 2.

dictionary = {'zero': 'ноль',
              'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'}


def num_translate_adv(key):
    return dictionary.get(key)

key = input('Введите число от 0 до 10 на английском языке, что бы узнать перевод: ')
if key[0].isupper():
    print(num_translate_adv(key.lower()).title())
else:
    print(num_translate_adv(key))