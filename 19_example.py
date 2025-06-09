# 1 Example № 21905

def f(n, m):
    if n >= 67: return m % 2 == 0# if ** ret *
    if m == 0: return 0# *
    h = [f(n + 1,m - 1),f(n + 4,m - 1),f(n * 3,m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 67) if f(s, 2)])
print('20)', [s for s in range(1, 67) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 67) if not f(s, 2) and f(s, 4)])

# 2 Example № 21418
print('2-------')

def f(s, m):
    if s <= 87: return m % 2 == 0
    if m == 0: return 0
    h = [f(s - 2, m - 1), f(s // 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(88, 10000) if f(s, 2)])
print('20)', [s for s in range(88, 10000) if not f(s, 1) and f(s, 3)])
print('20)', [s for s in range(88, 10000) if not f(s, 2) and f(s, 4)])

# 3 Example № 21714
print('3-------')

def f(s, m):
    if s >= 128: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s + 5, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 128) if f(s, 2)])
print('20)', [s for s in range(1, 128) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 128) if not f(s, 2) and f(s, 4)])

# 4 Example № 20907
print('4-------')

def f(a, b, m):
    if a + b >= 81: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19', [s for s in range(1, 74) if f(7, s, 2)])
print('20', [s for s in range(1, 74) if not f(7, s, 1) and f(7, s, 3)])
print('21', [s for s in range(1, 74) if not f(7, s, 2) and f(7, s, 4)])

# 5 Example № 20811
print('5-------')

def f(s, m):
    if s >= 51: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 51) if f(s, 2)])
print('20)', [s for s in range(1, 51) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 51) if not f(s, 2) and f(s, 4)])