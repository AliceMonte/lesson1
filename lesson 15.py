#1 В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
a = [5, 8, 2, 6, 21, 85, 15]
print('Наш список: ', a)
min1 = int(min(a))
print('Наименьший элемент 1: ', min1)
a.pop(min1)
min2 = int(min(a))
print('Наименьший элемент 2: ', min2)

#2 Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.
a = list(range(1, 20+1))
print('Наш список: ', a)
start = int(input('Введите начало интервала от 1 до 20: '))
end = int(input('Введите конец интервала от 1 до 20: '))
b = list(range(start, end+1))
print('Наш интервал: ', b)
for i in range(0, len(a)):
    for j in b:
        if a[i] == j:
            a.pop(i)
            a.append(0)
print(a)