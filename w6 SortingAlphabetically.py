# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.

# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
# Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
MyList = []
for list in inFile:
    list2 = list.split()
    MyList.append(list2)
MyList.sort()
for i in range(len(MyList)):
    print(MyList[i][0], MyList[i][1], MyList[i][3], file=outFile)
inFile.close()
outFile.close()
