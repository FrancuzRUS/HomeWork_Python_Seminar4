# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number = int(input('Введите желаемое количество элементов в последовательности: '))

origin_list = []
for i in range (1, number + 1):
    print('Добавить в список число: ')
    a = int(input())
    origin_list.append(a)
print('Первоначальный лист', origin_list)

sort_list = sorted(origin_list)
print('sort: ', sort_list)

new_list = []
if sort_list[0]!=sort_list[1]:
    new_list.append(sort_list[0])
if sort_list[-1]!=sort_list[-2]:
    new_list.append(sort_list[-1])

ind=1
prev_ind=0
next_ind=2
while ind<number+1:
    if sort_list[ind]!=sort_list[prev_ind]:
        if sort_list[ind]!=sort_list[next_ind]:
            new_list.append(sort_list[ind])
            ind+=1
            prev_ind+=1
            next_ind+=1
        else: break
    else:
        ind+=1
        prev_ind+=1
        next_ind+=1
print('Итоговая: ', new_list)



# number = int(input('Введите желаемое количество элементов в последовательности: '))

# def colcu_number(numm):                                             # создаем функцию / PS. Данная функция оказалась не нужна. задание понял не правильно. 
#     list = []                                                       # создаем списко
#     for i in range (1, numm+1):                                     # пробегаемся от первого до последнего элемента списка
#         print('Добавить в списко число: ')                          # 
#         a = int(input())                                            # заводим элемент
#         list.append(a)                                              # добавляем элемента в списко
#     print('первоначальный список: ', list)                          # выводим общий итоговый список
#     print('Список неповторяющихся значений: ',set(list))            # выводим список, но без повторяющихся значений 
# print(colcu_number(number))                                         # выводим результат работы нашей функции
# # Вопрос: Имелось ввиду что нужно выбрасывать одно из двух повторяющихя чисел или что необходимо убирать оба повторяющихся числа из последовательности? 
# # Пересмотрел семинар, вопрос отпал.

# def check_repeat(numm):

#--------------------------------------------------------------------------------
# часть проги создаёт и заполняет список

# number = int(input('Введите желаемое количество элементов в последовательности: '))

# origin_list = []
# for i in range (1, number + 1):
#     print('Добавить в список число: ')
#     a = int(input())
#     origin_list.append(a)
# print('Первоначальный лист', origin_list)

# origin_list = [1,6,5,3,2,4,5,6]
# print('origin_List = ', origin_list)
# #-----------------------------------------------------------------------
# # сортируем оригинальный список

# sorted_list = sorted(origin_list)
# print('сортированный лист = ',sorted_list)

#-------------------------------------------------------------------
# уникальные элементы списка

# unik_list = []
# for i in origin_list:
#   if i not in unik_list:
#     unik_list.append(i)
# print('unik_list = ',unik_list)

#---------------------------
# Идеи: 
# нужно сделать счетчик и если число встречается больше 1 раза его не нужно дабавлять в список. А если больше одного раза не добавлять

# new_list2 = []
# count = 0 
# for i in origin_list:
#     g = origin_list[i]
#     for j in origin_list:   # добавить while? while j < len.origin_list? 
#         h = origin_list[j]
#         if g == h:
#             count = count + 1
#             j = j + 1
#         else:
#             j = j + 1 
#     new_list2.append(origin_list[i])
# print('new list2 = ',new_list2)


# new_list = [] 
# x = [origin_list[0]]
# i = 0 
# j = 0 

# while i < len(origin_list):
#     if x != origin_list[j]:
#         new_list.append(origin_list[i])
#         j+=1
#     i+=1

# print('итоговый список:', new_list)

#-----------------------------------------




