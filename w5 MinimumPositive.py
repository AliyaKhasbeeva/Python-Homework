# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.

# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.

a = list(map(int, input().split()))
j = 1000
for i in a:
    if i > 0:
        if i < j:
            j = i
print(j)
