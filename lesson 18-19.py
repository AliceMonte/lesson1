#1 Дано 2 множества, содержащих названия IT-компаний. Найти только те компании, которые содержатся в обоих множествах.
i1 = {'EPAM', 'IBM', 'Wargaming', 'Andersen', 'iTechArt', 'OVERONE'}
print('IT компании в Республике Беларусь: ')
for i in i1:
    print(i, end=' ')
print()
i2 = {'IBM', 'HP Enterprise', 'Dell Technologies', 'Accenture', 'Oracle'}
print('Лучшие IT компании в мире: ')
for j in i2:
    print(j, end=' ')
print()
i3 = i1 & i2
print('Лучшая IT компания в Республике Беларусь: ')
for k in i3:
    print(k, end=' ')
print()


#2 Сгенерировать n множеств (нумерацию начать с 1).
# Вывести элементы, которые входят во все множества с номерами, кратными трём, но не входят в первое множество.
n = int(input('Введите кол-во множеств: '))
k = 3
s = {}
import random
for i in range(1, n+1):
    if i % k == 0:
        i = set(random.randint(1, 10) for i in range(10))
        print(i)
for s in range(1, n+1):
    if s % k == 0:
        s = set(random.randint(1, 10) for s in range(10))
        print(s)
i.intersection_update(s)
print('i= ', i)



