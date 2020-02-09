import math


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= math.sqrt(n):
            return n
        else:
            i += 1
    return i


def IsPrime(n):
    a = MinDivisor(n)
    if a == n:
        return True
    else:
        return False


n = int(input())
x = IsPrime(n)
if x:
    print("YES")
else:
    print("NO")
