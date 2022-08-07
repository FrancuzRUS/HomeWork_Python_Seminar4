# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import os

path_1 = os.path.join('Task5_Text1.txt')
path_2 = os.path.join('Task5_Text2.txt')
path_3 = os.path.join('Task5_Text3.txt')

with open(path_1, 'r') as p_1:
    data_1 = p_1.read()
data_1 = data_1.split()
print('Элементы уравнения из 1ого файла: ', data_1)

with open(path_2, 'r') as p_2:
    data_2 = p_2.read()
data_2 = data_2.split()
print('Элементы уравнения из 1ого файла: ', data_2)

data_1 = data_1[:-2]
data_2 = data_2[:-2]
data_3 = []

koef_1 = [int(data_1[0][:-4]), int((data_1[1]) + (data_1[2][:-4])), int((data_1[3]) + (data_1[4][:-2])), int((data_1[5]) + (data_1[6]))]
koef_2 = [int(data_2[0][:-4]), int((data_2[1]) + (data_2[2][:-4])), int((data_2[3]) + (data_2[4][:-2])), int((data_2[5]) + (data_2[6]))]

print('Коэфициенты из 1ого списка: ', koef_1)
print('Коэфициенты из 2ого списка: ', koef_2)

x_1 = int(data_1[0][:-4])
x_2 = int((data_1[1]) + (data_1[2][:-4]))
x_3 = int((data_1[3]) + (data_1[4][:-2]))
x_4 = int((data_1[5]) + (data_1[6]))

y_1 = int(data_2[0][:-4])
y_2 = int((data_2[1]) + (data_2[2][:-4]))
y_3 = int((data_2[3]) + (data_2[4][:-2]))
y_4 = int((data_2[5]) + (data_2[6]))

x1 = x_1 + y_1
x2 = x_2 + y_2
x3 = x_3 + y_3
x4 = x_4 + y_4

# data_3 = (x_1 + y_1), (x_2 + y_2), (x_3 + y_3), (x_4 + y_4) 

# data_3 = x1, x2, x3, x4

data_3.append(x1)
data_3.append(x2)
data_3.append(x3)
data_3.append(x4)

with open(path_3, 'w') as new_file:
    new_file.write(f'{x1}')
    new_file.write('*x^3')
    new_file.write(' + ')
    new_file.write(f'{x2}')
    new_file.write('*x^2')
    new_file.write(' + ')
    new_file.write(f'{x3}')
    new_file.write(' + ')
    new_file.write(f'{x4}')
    new_file.write(' = ')
    new_file.write(' 0 ')

print('Сумма Коэфициентов равна = ',data_3) 

with open(path_3, 'r') as p_3:
    data_3 = p_3.read()


print('Сумма многочленов : ', data_3)

#-----------------------------------




