# 1 Example № 21898

for n in range(4, 10000):
    s = '1' + n * '9'# 1999999 or 19999
    while '19' in s or '399' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '399' in s:
            s = s.replace('399', '91', 1)
        if '999' in s:
            s = s.replace('999', '3', 1)
    sm = sum(map(int, s))# сумма всех цифр в строке
    if sm == 33:
        print(n)
        break

# 2 Example № 21411

for n in range(4, 10000):
    s = '3' + n * '1'
    while '31' in s or '211' in s or '1111' in s:
        s = s.replace('31', '1', 1)
        s = s.replace('211', '13', 1)
        s = s.replace('1111', '2', 1)
    sm = sum(map(int, s))
    if sm == 15:
        print(n)
        break

# 3 Example № 21707

for n in range(4, 10000):
    s = '4' + n * '2'
    while '42' in s or '8222' in s or '2222' in s:
        s = s.replace('42', '2', 1)
        s = s.replace('8222', '24', 1)
        s = s.replace('2222', '8', 1)
    sm = sum(map(int, s))
    if sm == 110:
        print(n)
        break
