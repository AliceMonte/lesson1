import m1, m2, m3
while True:
    c = input('Для выхода нажмите 0. Считать площадь - круга, прямоугольника, треугольника: ')
    if c == 'круга':
        a = int(input('Введите длину радиуса:'))
        print('Площадь круга равна: ', m1.pl_crug(a))
    elif c == 'прямоугольника':
        a = int(input('Введите длину прямоугольника:'))
        b = int(input('Введите ширину прямоугольника:'))
        print('Площадь прямоугольника равна: ', m2.pl_prim(a, b))
    elif c == 'треугольника':
        a = int(input('Введите основание треугольника:'))
        b = int(input('Введите высоту треугольника:'))
        print('Площадь треугольника равна: ', m3.pl_treug(a, b))
    elif c == '0':
        break