# ∧ AND
# ∨ OR
# ≡ ==
# ¬ NOT
# → <=

# 1 Example № 21888

# F=(x∧¬y)∨(y≡z)∨w

from itertools import permutations, product# *

def f(x, y, w, z):# **
    return (x and (not y)) or (y == z) or w# F=(x∧¬y)∨(y≡z)∨w


for x1, x2, x3, x4 in product([0, 1], repeat=4):# changing repeat and the number of variables
    t = (# перепиши таблицу из задания
        (x1, x2, 1, x3, 0),#
        (0, 0, 0, 1, 0),#
        (1, 0, x4, 1, 0)#
    )#
    if len(t) == len(set(t)):# *
        for p in permutations('xywz', r=4):# *
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):# *
                print(*p)# *

# 2 Example № 21401

# F=x∧(z→w)∧¬y

from itertools import permutations, product# *

def f(x, y, w, z):# **
    return x and (z <= w) and (not y)# F=x∧(z→w)∧¬y

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):# changing repeat and the number of variables
    t = (# таблица в задании
        (x1, x2, 1, x3, 1),#
        (x4, 1, 0, x5, 1),#
        (1, 0, x6, x7, 1)#
    )#
    if len(t) == len(set(t)):# *
        for p in permutations('xywz', r=4):# *
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):# *
                print(*p)# *

# 3 Example № 21697

# F=¬(x→y)∨(z≡w)∨z

from itertools import permutations, product# *

def f(x, y, w, z):# **
    return (not (x <= y)) or (z == w) or z# F=¬(x→y)∨(z≡w)∨z


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (# таблица в задании
        (0, 0, x1, x2, 0),
        (x3, x4, 1, x5, 0),
        (x6, 1, 0, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4):# *
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):# *
                print(*p)# *