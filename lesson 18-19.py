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
mn = list()
ml = list()
k = 3
import random
for i in range(n):
    a = set(random.randint(1, 15) for a in range(10))
    mn.append(a)
print(mn)
for i in range(n):
    if i % k == 0:
        ml.append(mn[i])
print(ml)
f = 2
z = 1
y = ml[1].intersection(ml[2])
t = ml[0]
for i in range(len(ml)):
    while f < len(ml):
        r = ml[z].intersection(ml[f])
        z += 1
        f += 1
u = (r & y) - t
if u != set():
    print('Элементы,которые входят во множества,кратные 3 и не входят в первое:', u)
else:
    print('Совпадений нет')




