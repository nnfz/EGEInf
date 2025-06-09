# 1 Example № 21710

def f(x):# Init *
    B = 36 <= x <= 75# otrezok
    C = 60 <= x <= 110# otrezok
    A = a1 <= x <= a2# new otrezok
    return (not A) <= (B == C)# ¬(x∈A)→((x∈B)≡(x∈C))

r = []# result *
d = [y for x in [36, 60, 75, 110] for y in [x, x + 0.1, x - 0.1]]# range
for a1 in d:# *
    for a2 in d:# *
        if a2 >= a1 and all(f(x) == 1 for x in d):# f(x) == 1 or f(x) == 0 see task
            r += [a2 - a1]# push otrezok *
print(round(min(r)))# смотри в задание

# 2 Example № 20961

def f(x):# init *
    P = 15 <= x <= 142# otrezok
    Q = 38 <= x <= 167# otrezok
    A = a1 <= x <= a2# new otrezok
    return (not (Q <= (((not A) and P) <= (not Q))))# ¬((x∈Q)→((¬(x∈A)∧(x∈P))→¬(x∈Q)))

r = []# result *
d = [y for x in [15, 38, 142, 167] for y in [x, x + 0.1, x - 0.1]]# range
for a1 in d:# *
    for a2 in d:# *
        if a2 >= a1 and all(f(x) == 0 for x in d):# f(x) == 1 or f(x) == 0 see task
            r += [a2 - a1]# * суем наш отрезок
print(round(min(r)))# смотри в задание

# 3 Example [коньюкция] № 21901

def f(x):
    return ((x&52 != 0) and (x&48 == 0)) <= (not(x&A == 0))

for A in range(100):
    if all(f(x) == 1 for x in range(10000)):
        print(A)
        break

# 4 Example № 20905

def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

r = []
d = [y for x in [17, 29, 58, 80] for y in [x, x+0.1, x-0.1]]

for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 1 for x in d):
            r += [a2 - a1]

print(round(min(r)))

# 5 Example № 20809
def f(x):
    B = 60 <= x <= 80
    return (x % A == 0) or ((B) <= (x % 22 != 0))

for A in range(1, 10000):
    if all(f(x) == 1 for x in range(1, 1000000)):
        print(A)
