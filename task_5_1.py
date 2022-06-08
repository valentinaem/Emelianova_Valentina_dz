# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1

def odd_nums(n):
    for num in range(1, n + 1):
        yield num

odd_to_15 = odd_nums(15)
print(next(odd_to_15))


n = 5
odd_nums = (num for num in range(1, n + 1))
print(next(odd_nums))
