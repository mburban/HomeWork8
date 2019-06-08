# Найдите сумму и произведение элементов списка. Результаты вывести на экран;

import random
my_list = [i for i in range(1, random.randint(5, 25))]
print(my_list)
list_sum = 0
list_mult = 1

for j in my_list:
    list_sum = j + list_sum
    list_mult = j * list_mult
print(list_sum)
print(list_mult)
