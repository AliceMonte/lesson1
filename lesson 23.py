#Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем.
#Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
#Вывод значений элементов массива должен происходить в основной ветке программы.
#1
a = int(input('Введите кол-во элементов: '))
def addtolist(list1,min,max):
    import random
    for i in range(a):
        list1[i] = int(random.randint(min, max))
    list1.sort()
randomlist = [0] * a
m = int(input('Введите начало диапазона: '))
n = int(input('Введите конец диапазона: '))
addtolist(randomlist, m, n)
print(randomlist)

#2
b = int(input('Введите кол-во элементов: '))
def random(mn,mx):
    import random
    return (random.randint(mn, mx))
list1 = []
m = int(input('Введите начало диапазона: '))
n = int(input('Введите конец диапазона: '))
for i in range(b):
    list1.append(random(m, n))
list1.sort()
print(list1)