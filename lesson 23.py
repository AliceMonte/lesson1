#Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем.
#Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать.
#Вывод значений элементов массива должен происходить в основной ветке программы.
a = int(input('Введите кол-во элементов: '))
def addtolist(list1,min,max):
    import random
    for i in range(a):
        list1[i] = int(random.randint(min, max))
    list1.sort()
randomlist = [0] * a
m = int(input('Введите начало диапазона: '))
n = int(input('Введите начало диапазона: '))
addtolist(randomlist,m,n)
print(randomlist)