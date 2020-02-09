# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.
# Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске
# определит максимальное число пользователей, чьи данные можно поместить в архив.

# Формат ввода
# Программа получает на вход в одной строке число S – размер свободного места на диске
# (натуральное, не превышает 10000), и число N – количество пользователей (натуральное, не превышает 100),
# после этого идет N чисел - объем данных каждого пользователя (натуральное, не превышает 1000),
# записанных каждое в отдельной строке.

# Формат вывода
# Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.


x = list(map(int, input().split()))
s = x[0]
n = x[1]
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
asum = 0
i = 0
for j in range(n):
    if j != n:
        asum += a[j]
        if asum > s:
            print(i)
            break
        elif asum <= s and j == n - 1:
            i += 1
            print(i)
        else:
            i += 1
