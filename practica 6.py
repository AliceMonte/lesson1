#Написать функцию, которая определяет количество разрядов введённого целого числа.
def razr(chislo):
    r = 0
    while chislo > 0:
        chislo = chislo//10
        r += 1
    return r
n = abs(int(input('Введите число: ')))
print('Количество разрядов:', razr(n))
