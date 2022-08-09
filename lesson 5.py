#1
i = 5
print(type(i))
print (i+1)
#2
i = 5
print(type(i))
print ('Значение составляет',i)
#3
name = 'Дима'
print(type(name))
print ('Привет,',name)
#4
name = input('Введите имя:')
print(type(name))
print ('Привет,',name)
#5
a= 2.3
b= 3.4
c=a+b
print(type(a),type(b))
print('{0:.2}'.format(c))
#6
number = 0.5
print(type(number))
if number<1:
    print (True)
else:
    print (False)
#7
print ('f<d')
f = int(input('Число f:'))
d = int (input('Число d:'))
if f<d :
    print ('Выражение верное')
else:
    print ('Неверно')
#8
name = 'Герда'
running = True
print(type(running))
while running:
    guess = str(input('Угадай моё имя : '))
    if guess == name:
        print('Поздравляю, вы угадали.')
        running = False #
    else:
        print('Нет, подумай ещё.')
else:
    print('Завершено.')
#9
g=None
print(type(g))
if g is None:
    print ('g is None')
else:
    print ('g is not None')
#10
a = [1, 2, 7, 9, 10, 12, 13, 21, 34, 55, 89]
print(type(a))
print([elem for elem in a if elem < 11])
