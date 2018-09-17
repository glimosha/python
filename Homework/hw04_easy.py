
__author__ = 'Блинов Андрей Игоревич'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [1, 2, 4, 0]
sqr_numbers = []
for number in numbers:
    sqr_numbers.append(number ** 2)
print(sqr_numbers)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ["банан", "яблоко", "груша", "мандарин", "инжир", "папайя"]
fruits_2 = ["дыня", "яблоко", "мандарин", "инжир", "банан", "нектарин"]
fruits = []
for _ in fruits_1:
    if _ in fruits_2:
        fruits.append(_)
        fruits_1.remove(_)
        fruits_2.remove(_)
for _ in fruits_2:
    if _ in fruits_1:
        fruits.append(_)
print(fruits)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

def x_3(a):
    lst_x_3 = []
    for number in a:
        b = number % 3
        if b == 0:
            lst_x_3.append(number)
    return lst_x_3

def positive(a):
    lst_positive = []
    for number in a:
       if number >= 0:
           lst_positive.append(number)
    return lst_positive

def non_x_4(a):
    lst_non_x_4 = []
    for number in a:
        b = number % 4
        if b != 0:
            lst_non_x_4.append(number)
    return lst_non_x_4

lst = []
for _ in range(10):
    lst.append(random.randint(-100, 100))

print('числа', lst)
print('числа кратные 3', x_3(lst))
print('положительные числа', positive(lst))
print('числа не кратные 4', non_x_4(lst))
