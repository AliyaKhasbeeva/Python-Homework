# В списке все элементы попарно различны. Поменяйте местами минимальный и максимальный элемент этого списка.

# Формат вводa
# Вводится список целых чисел. Все числа списка находятся на одной строке.


a = list(map(int, input().split()))
mylen = len(a)
maxi = 0
mini = 1000000
posMax = 0
posMin = 0
for i in range(0, mylen):
    if a[i] > maxi:
        maxi = a[i]
        posMax = i
    if a[i] < mini:
        mini = a[i]
        posMin = i
x = a[posMax]
a[posMax] = a[posMin]
a[posMin] = x
print(*a)
