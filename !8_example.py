# 1 Example № 21894

from itertools import *# *

num = list(permutations('0123456789', r=4))# ** перебираем все варики без повторений
c = 0# * счетчик

for n in num:# * разделяем варики по отдельным строкам
    nums = ''.join(n)# * соединяем в строку без всего ('(1), (3)') => 13
    if nums[0] != '0':# в числе 0 не может быть в начале
        nums = nums.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')# заменяем все четные на 0
        nums = nums.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')# заменяем все нечетные на 1
        if '00' not in nums and '11' not in nums:# проверяем, чтобы они не были рядом
            c += 1# счетчик
print(c)

# 2 Example № 21407

from itertools import *# *

wor = list(product('ДГИАШЭ', repeat=5))# ** перебираем все варики
c = 0# * счетчик

for w in wor:# * разделяем варики по отдельным строкам
    word = ''.join(w)# * соединяем в строку без всего
    if word[0] != 'И' and word[0] != 'А' and word[0] != 'Э':# проверяем гласные в начале
        # так как слово 5-ти буквенное, мы просто хуячим индекс
        if word[4] != 'Д' and word[4] != 'Г' and word[4] != 'Ш':# проверяем согласные в конце
            c += 1# счетчик
print(c)

# 3 Example № 21703 GAVNO

from itertools import *

st = list(product('АБДЕОП', repeat=6))

c = 0

for s in st:
    a = ''.join(s)
    b = str(c) + '. ' + a
    c += 1
    if a[0] == 'О' and len(set(a)) == 6 and c % 2 == 0:
        print(str(c) + '. ' + a)

# 4 Example № 20898

from itertools import *

num = list(product('012345678', repeat=5))

c = 0
for n in num:
    a = ''.join(n)
    if a[0] != '0' and a.count('0') == 1:
        if '01' not in a and '03' not in a and '05' not in a and '07' not in a and '10' not in a and '30' not in a and '50' not in a and '70' not in a:
            c += 1
print(c)

# 5 Example № 20857

from itertools import *

na = list(product('012345678', repeat=6))

c = 0
for n in na:
    cc = str(c)
    a = ''.join(n)
    if a[0] != '0':
        c += 1
        if c%10 == 5:
            na = a
            na = na.replace('1', '3').replace('3', '5').replace('5', '7')
            if '77' not in na:
                print(a)
