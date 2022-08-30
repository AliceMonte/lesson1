#1
n = int(input('Число из ряда Фибоначчи: '))
f = 1
c1 = 1
c2 = 2
while f < n-1:
    c3 = c1 + c2
    c1 = c2
    c2 = c3
    f += 1
print(c3)

#2
x = int(input('Факториал для числа: '))
a = 1
factorial = 1
while a <= x:
    factorial *= a
    a += 1
print(factorial)