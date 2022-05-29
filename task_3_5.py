import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    humor = []
    for i in range(n):
        one_world = random.choice(nouns)
        nouns.remove(one_world)
        two_world = random.choice(adverbs)
        adverbs.remove(two_world)
        three_world = random.choice(adjectives)
        adjectives.remove(three_world)
        humor.append(f'{one_world} {two_world} {three_world}')
    return humor

print(get_jokes(3))


