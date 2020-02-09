#Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

import math


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= math.sqrt(n):
            return n
        else:
            i += 1
    return i


n = int(input())
print(MinDivisor(n))
