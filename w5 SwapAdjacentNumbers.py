# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.

a = list(map(int, input().split()))
mylen = len(a)
for i in range(0, mylen - 1, 2):
    j = a[i]
    a[i] = a[i + 1]
    a[i + 1] = j
print(*a)