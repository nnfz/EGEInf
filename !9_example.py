# IMPORTANT https://www.youtube.com/watch?v=2C8ZF8tfM1E !!!

# 1 Example № 21895

c = 0# counter *
for line in open('task_files/9_Example-1.txt'):# * импортируем файл ('**')
    a = [int(x) for x in line.split()]# * берем числа с каждой новой строки
    ass = sorted(a)# сортируем по возрастанию (12, 43, 145)
    if len(set(ass)) == 5:# длина строки
        if ass[3] + ass[4] <= ass[0] + ass[1] + ass[2]:# сумма 2 наибольших <= сумме 3 наименьших
            c += 1# * счетчик
print(c)

# 2 Example № 21408

c = 0# * счетчик
for line in open('task_files/9_Example-2.txt'):# * импортируем файл ('**')
    a = [int(x) for x in line.split()]# * берем числа с каждой новой строки
    a3 = [x for x in a if a.count(x) == 3]# проверка чисел на повторение 3 раза
    a1 = [x for x in a if a.count(x) == 1]# проверка чисел на не повторение
    if len(a3) == 6 and len(a1) == 1 and max(a3) > a1[0]:# условие
        c += 1# * счетчик
print(c)

# 3 Example № 21704

for line in open('task_files/9_Example-3.txt'):# * импортируем файл ('**')
    a = [int(x) for x in line.split()]# * берем числа с каждой новой строки
    ass = sorted(a)# сортируем по возрастанию (12, 43, 145)
    if  a[0] > a[1] > a[2] > a[3] > a[4] > a[5] > a[6]:# сортируем по убыванию (145, 124, 12)
        if (ass[0] + ass[6])/2 > (ass[1] + ass[2] + ass[3] + ass[4] + ass[5]) / 5:# среднее арифметичекое первого и последнего > среднего арифметического остальных
            print(a, sum(a))
            break# останавливаем на первом шагу

# 4 Example № 20899

c = 0
for line in open('task_files/9_Example-4.txt'):
    a = [int(x) for x in line.split()]
    a2 = [x for x in a if a.count(x) == 2]
    ass = sorted(a)
    if len(a2) == 2:
        if ass[3] < ass[0] + ass[1] + ass[2]:
            c += 1
print(c)

# 5 Example № 20955

c = 0
for line in open('task_files/9_Example-5.txt'):
    a = [int(x) for x in line.split()]
    a2 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2) == 4 and len(a1) == 4:
        if (a2[0] + a2[1] + a2[2] + a2[3]) >= (a1[0] + a1[1] + a1[2] + a1[3]) * 2:
            c += 1
print(c)