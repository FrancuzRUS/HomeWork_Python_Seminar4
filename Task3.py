# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number = int(input('Введите желаемое количество элементов в последовательности: '))


def colcu_number(numm):                                             # создаем функцию 
    list = []                                                       # создаем списко
    for i in range (1, numm+1):                                     # пробегаемся от первого до последнего элемента списка
        print('Добавить в списко число: ')                          # 
        a = int(input())                                            # заводим элемент
        list.append(a)                                              # добавляем элемента в списко
    print('первоначальный списко: ', list)                          # выводим общий итоговый список
    print('Список неповторяющихся значений: ',set(list))            # выводим список, но без повторяющихся значений 

print(colcu_number(number))                                         # выводим результат работы нашей функции

# Вопрос: Имелось ввиду что нужно выбрасывать 1 из 2 повторяющихя чисел или что необходимо убирать 2 повторяющихся числа из последовательности? 