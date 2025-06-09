# 1 Example № 21900

for x in range(1, 2301):
    c = 0
    a = 7 ** 350 + 7**150 - x
    while a > 0:
        if a % 7 == 0:
            c += 1
        a //= 7
    if c == 200:
        print(x)

# 2 Example № 21413

from string import *

for x in printable[:21]:
    a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if a % 20 == 0:
        print(x, a//20)

# 3 Example № 21709

m = []
for x in range(1, 3001):
    a = 4**210+4**110-x
    c = 0
    while a > 0:
        if a % 4 == 0:
            c += 1
        a //= 4
    m.append(c)
    if c == 105:
        print(x)
        break
print(max(m))

# 4 Example № 20904

m = []
for x in range(1, 2031):
    a = 7**170 + 7**100 - x
    c = 0
    while a > 0:
        if a % 7 == 0:
            c += 1
        a //= 7
    m.append(c)
    if c == 73:
        print(x)

# 5 Example № 20904

m = []
for x in range(1, 2031):
    a = 3**100 - x
    c = 0
    while a > 0:
        if a % 3 == 0:
            c += 1
        a //= 3
    m.append(c)
    if c == 1:
        print(x)