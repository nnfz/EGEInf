# 1 Example № 21891

s = []# spisok
for n in range(1, 10000):# int n
    b = bin(n)[2:]# * | IMPORTANT [2:] - 0b****
    b += str(sum(map(int, b)) % 2)# '0101101' + sum '0101101' / 2 ostatok
    b += str(sum(map(int, b)) % 2)# '0101101' + sum '0101101' / 2 ostatok
    i = int(b, 2)# 2 to 10
    if i > 253:# if
        s.append(n)# push to spisok
print(min(s))# min is not important
print(s)# min is not important

# 2 Example № 21700 with number system

def co(i, m):# convert to any number system
    st = ''
    while i > 0:
        st += str(i % m)
        i //= m
    return st[::-1]# '123' to '321'

s = []# spisok
for n in range(3, 200):# int n
    b = co(n, 3)# convert to 3 system
    if n % 3 == 0:
        b += b[-2] + b[-1]# + last 2 numbers
    else:
        b += co(((n%3)*3), 3)
    i = int(b, 3)# 3 to 10
    if i <= 150:# if
        s.append(n)# push to spisok
print(max(s))# max is not important
print(s)# max is not important

# 3 Example № 21404
s = []
for n in range(1000):
    b = bin(n)[2:]# * | IMPORTANT [2:] - 0b****
    if sum(map(int, b)) % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    i = int(b, 2)
    if i > 480:
        s.append(n)
print(min(s))# min is not important
print(s)# min is not important