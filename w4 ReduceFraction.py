# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких, что (n / m) = (p / q) и
# дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


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


def ReduceFraction(n, m):
    nod = gcd(n, m)
    n2 = n // nod
    m2 = m // nod
    return n2, m2


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
