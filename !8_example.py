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