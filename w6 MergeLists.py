# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.

# Формат ввода
# Программа получает на вход два неубывающих списка, каждый в отдельной строке.

# Формат вывода
# Программа должна вывести последовательность неубывающих чисел, полученных объединением двух данных списков.


def merge(a, b):
    c = []
    i = 0
    j = 0
    while i != len(a) or j != len(b):
        if i == len(a):
            c.append(b[j])
            j += 1
        elif j == len(b):
            c.append(a[i])
            i += 1
        else:
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = merge(a, b)
print(*d)
