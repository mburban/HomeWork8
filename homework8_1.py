# Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию, которая переставляет его элементы в
# случайном порядке (например, 99 11 43 19 … 7 91 3 1).
# 	Примечание: использовать метод random.shuffle не допускается.


def list_randomizer(list_var, list_len):
    import random
    list_randomizing = random.sample(list_var, list_len)
    return list_randomizing


list_for_random = [i for i in range(1, 100, 2)]

randomized_list = list_randomizer(list_for_random, len(list_for_random))

print('Список до переставления элементов:\n', list_for_random)
print('Список после переставления элементов:\n', randomized_list)
