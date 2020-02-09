# Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех этих чисел, не используя цикл.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее окончания).

def rec():
    n = int(input())
    if n == 0:
        return 0
    return n + rec()


print(rec())
