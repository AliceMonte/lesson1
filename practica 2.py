#1
try:
    q = input('Введите число: ')
    if len(q) == 2:
        sum = int(str(q)[0]) + int(str(q)[1])
        mn = int(str(q)[0]) * int(str(q)[1])
        print('Сумма чисел равна', sum)
        print('Произведение чисел равно', mn)
    elif len(q) == 3:
        sum = int(str(q)[0]) + int(str(q)[1]) + int(str(q)[2])
        mn = int(str(q)[0]) * int(str(q)[1]) * int(str(q)[2])
        print('Сумма чисел равна', sum)
        print('Произведение чисел равно', mn)
    elif len(q) == 4:
        sum = int(str(q)[0]) + int(str(q)[1]) + int(str(q)[2]) + int(str(q)[3])
        mn = int(str(q)[0]) * int(str(q)[1]) * int(str(q)[2]) * int(str(q)[3])
        print('Сумма чисел равна', sum)
        print('Произведение чисел равно', mn)
    elif len(q) == 5:
        sum = int(str(q)[0]) + int(str(q)[1]) + int(str(q)[2]) + int(str(q)[3]) + int(str(q)[4])
        mn = int(str(q)[0]) * int(str(q)[1]) * int(str(q)[2]) * int(str(q)[3]) * int(str(q)[4])
        print('Сумма чисел равна', sum)
        print('Произведение чисел равно', mn)
    else:
        print('Ой, ну не надо вводить такие числа большие, я же не калькулятор!')
except ValueError:
    print('Введите число, а не строку')

#2
try:
    a = int(input('Введите начальное натуральное число: '))
    b = int(input('Введите последнее натуральное число: '))
    c = int(input('Введите шаг: '))
    print(*range(a, b + 1, c))
except ValueError:
    print('Введите число, а не строку')
