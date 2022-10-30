#Найти сумму цифр числа с помощью рекурсии. 112 = 4
n = int(input('Введите число: '))
def summchisla(n):
    if n < 10:
        return n
    else:
        return (n%10) + summchisla(n//10)
print(summchisla(n))
