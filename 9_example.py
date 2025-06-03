# IMPORTANT https://www.youtube.com/watch?v=2C8ZF8tfM1E !!!

# 1 Example № 21895

c = 0# counter *
for line in open('task_files/9_Example-1.txt'):# import file *('**')
    a = [int(x) for x in line.split()]# split int to lines *
    ass = sorted(a)# sort ints (12, 43, 145)
    if len(set(ass)) == 5:# len line
        if ass[3] + ass[4] <= ass[0] + ass[1] + ass[2]:# sum 2 max <= sum 3 min
            c += 1# counter *
print(c)

# 2 Example № 21408

c = 0# counter *
for line in open('task_files/9_Example-2.txt'):# import file *('**')
    a = [int(x) for x in line.split()]# split int to lines *
    a3 = [x for x in a if a.count(x) == 3]# count int if repeat 3 times
    a1 = [x for x in a if a.count(x) == 1]# repeat 1 times or no repeat
    if len(a3) == 6 and len(a1) == 1 and max(a3) > a1[0]:# if
        c += 1# counter *
print(c)

# 3 Example № 21704

for line in open('task_files/9_Example-3.txt'):# import file *('**')
    a = [int(x) for x in line.split()] # split int to lines *
    ass = sorted(a)# sort ints (12, 43, 145)
    if  a[0] > a[1] > a[2] > a[3] > a[4] > a[5] > a[6]:# sort ints (145, 124, 12)
        if (ass[0] + ass[6])/2 > (ass[1] + ass[2] + ass[3] + ass[4] + ass[5]) / 5:# mean(min+max) > mean(other)
            print(a, sum(a))
            break# stop on first step