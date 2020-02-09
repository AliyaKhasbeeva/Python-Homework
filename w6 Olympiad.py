#В олимпиаде участвовало N человек. Каждый получил определенное количество баллов,
# при этом оказалось, что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.

#Формат ввода
#Программа получает на вход число участников олимпиады N.
# Далее идет N строк, в каждой строке записана фамилия участника,
# затем, через пробел, набранное им количество баллов.


n = int(input())
MyList = []
for i in range(n):
    v = list(input().split())
    MyList.append((int(v[1]) * -1, v[0]))
MyList.sort()
for j in MyList:
    print(j[1])