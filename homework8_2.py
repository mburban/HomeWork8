# Создайте список из 11 случайных целых чисел из отрезка [-1;1]. Передайте его в функцию, которая определит какой
# элемент встречается в списке чаще всего и вернет этот элемент. Однако, если два каких-то элемента встречаются
# одинаковое количество раз, то вернуть None, а не самый часто встречающийся элемент, даже если дублирующиеся элементы
# не максимальны!

#       Например:
# 		для [1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0] надо вернуть None
# 		для [1, 1, 1, 1, -1, 1, 1, -1, 0, 0, 0] надо вернуть 1

import random
import math


def most_often_item(my_list):
    i = 0
    var_pos_one = 0
    var_neg_one = 0
    var_zero = 0

    for i in my_list:
        if i == 1:
            var_pos_one += i
        elif i == 0:
            var_zero += 1
        else:
            var_neg_one += int(math.fabs(i))
    if var_pos_one > var_zero and var_pos_one > var_neg_one:
        return 'Элемент 1 встречается чаще всего'
    elif var_neg_one > var_pos_one and var_neg_one > var_zero:
        return 'Элемент -1 встречается чаще всего'
    elif var_zero > var_neg_one and var_zero > var_pos_one:
        return 'Элемент 0 встречается чаще всего'
    else:
        return None


my_list = [random.randint(-1, 1) for _ in range(11)]
print(my_list)


print(most_often_item(my_list))