# # 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# # (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# # Пример:
# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
import random

path = os.path.join('Task4_Text.txt')

# with open(path, 'r') as f:
#     data = f.readlines()
# print(data)

razdelitel=''
k = int(input('Введите желаемую степень многочлена: '))
mnogochlen=''
for i in range(0, k+1):
    koeff=random.randint(0, 101)
    print ('степень', {i}, ' при коэффициенте',koeff)
    if koeff!=0:
        if i==0:
            chlen = [' + ', koeff]
            # chlen = [' +', koeff, ' = 0']
            chlen=[str(j)for j in chlen] 
            finish_chlen=razdelitel.join(chlen)
            mnogochlen= finish_chlen+mnogochlen

        elif i==k:
            chlen = [koeff, '*x', '^', i]
            chlen=[str(j)for j in chlen]
            finish_chlen=razdelitel.join(chlen)
            mnogochlen= finish_chlen+mnogochlen

        elif i==1:
            chlen = [' + ', koeff, '*x']
            chlen=[str(j)for j in chlen]
            finish_chlen=razdelitel.join(chlen)
            mnogochlen= finish_chlen+mnogochlen

        else:
            chlen = [' + ', koeff, '*x', '^', i]
            chlen=[str(j)for j in chlen]
            finish_chlen=razdelitel.join(chlen)
            mnogochlen= finish_chlen+mnogochlen
mnogochlen = mnogochlen + ' = 0'

print (mnogochlen)

with open(path, 'a') as f:
     f.write(f'{mnogochlen}\n')