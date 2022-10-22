from l25 import sumrazn, prodel
while True:
    c = input('Для выхода нажмите 0. Выберите действие: +,-,*,/ : ')
    if c == '+':
        a = int(input('Введите число 1:'))
        b = int(input('Введите число 2:'))
        print('Сумма равна: ', sumrazn.summ(a, b))
    elif c == '-':
        a = int(input('Введите число 1:'))
        b = int(input('Введите число 2:'))
        print('Разность равна: ', sumrazn.razn(a, b))
    elif c == '*':
        a = int(input('Введите число 1:'))
        b = int(input('Введите число 2:'))
        print('Произведение равно: ', prodel.pro(a, b))
    elif c == '/':
        a = int(input('Введите число 1:'))
        b = int(input('Введите число 2:'))
        print('Деление равно: ', prodel.delit(a, b))
    elif c == '0':
        break