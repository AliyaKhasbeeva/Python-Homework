# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).


def gcd(a, b):
    if a != 0 and b != 0:
        if a > b:
            res = gcd(a % b, b)
            return res
        else:
            res = gcd(a, b % a)
            return res
    else:
        return a + b


a = int(input())
b = int(input())
print(gcd(a, b))
