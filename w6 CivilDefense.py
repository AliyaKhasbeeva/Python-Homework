# Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки.
# Известно, что все n селений Тридесятой области находятся вдоль одной прямой дороги.
# Вдоль дороги также расположены m бомбоубежищ, в которых жители селений могут укрыться на случай ядерной атаки.

# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.

# Формат ввода
# В первой строке вводится число n - количество селений (1 <= n <= 100000).
# Вторая строка содержит n различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до i-го селения.
# В третьей строке входных данных задается число m - количество бомбоубежищ (1 <= m <= 100000).
# Четвертая строка содержит m различных целых чисел, i-е из этих чисел задает расстояние от начала
# дороги до i-го бомбоубежища. Все расстояния положительны и не превышают 10⁹.
# Селение и убежище могут располагаться в одной точке.

# Формат вывода
# Выведите n чисел - для каждого селения выведите номер ближайшего к нему бомбоубежища.
# Бомбоубежища пронумерованы от 1 до m в том порядке, в котором они заданы во входных данных.


n = int(input())
vill = list(map(int, input().split()))
m = int(input())
bomb = list(map(int, input().split()))
villagedist = []
bombdist = []
for i in range(n):
    vdist = (vill[i], i + 1)
    villagedist.append(vdist)
for j in range(m):
    bdist = (bomb[j], j + 1)
    bombdist.append(bdist)
villagedist.sort()
bombdist.sort()
posbomb = []
selectedbomb = 0
for v in villagedist:
    mindist = 1000000000000000000
    positbomb = 0
    for b in range(selectedbomb, m):
        dist = abs(v[0] - bombdist[b][0])
        if dist <= mindist and b == m - 1:
            positbomb = (v[1], bombdist[b][1])
            posbomb.append(positbomb)
            break
        elif dist <= mindist:
            mindist = dist
            positbomb = (v[1], bombdist[b][1])
            selectedbomb = b
        else:
            posbomb.append(positbomb)
            break
posbomb.sort()
posb = []
for i in posbomb:
    posb.append(i[1])
print(*posb)
