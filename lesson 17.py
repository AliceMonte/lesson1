#1 Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные. Результат вывести в виде кортежа.
#Первый элемент
s = tuple(input('Введите любое слово: '))
print(s)
s = list(s)
print(s)
s = list(s[0:1])
s = tuple(s)
print(s)

#1.2
#Первые два элемента
a = tuple(input('Введите любое слово: '))
print(a)
a = list(a)
print(a)
del a[2:len(a)]
a = tuple(a)
print(a)

#1.3
a = tuple(input('Введите любое слово: '))
print(a)
a = list(a)
print(a)
for i in range(len(a)):
    if i > 1:
        a.pop(i)
a = tuple(a)
print(a)
