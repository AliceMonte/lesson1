min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))
summ = 0
if min < max:
    for i in range(min, max + 1):
        summ += i
    print(summ)
else:
    print('Вы ввели неверные значения')