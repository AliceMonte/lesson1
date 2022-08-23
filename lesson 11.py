#1
try:
    mechta = 'Хочу' + 100000
except TypeError:
    print('Доучись и получи')
    try:
        month = 12
        cash = 'мало денюжек'
        res = int(month) * int(cash)
    except ValueError:
        print('Конечно мало')
#2
try:
    print('Вводите целые числа от 1')
    print('Мой день рождения:')
    year = input('Я родилась в году ')
    month = input('В месяце ')
    date = input('Числа ')
    print('Сегодня:')
    year_t = input('год ')
    month_t = input('месяц ')
    date_t = input('число ')
    let = ((int(year_t) - int(year)) * 12 + int(month_t) - int(month)) // 12
    if let == 1 or let == 21 or let == 31 or let == 41 or let == 51 or let == 61 or let == 71 or let == 81 or let == 91:
        print('Мне', let, 'год')
    elif 1 < let <= 4 or 21 < let <= 24 or 31 < let <= 34 or 41 < let <= 44 or 51 < let <= 54 or 61 < let <= 64 or 71 < let <= 74 or 81 < let <= 84 or 91 < let <= 94:
        print('Мне', let, 'года')
    elif 5 == let <= 20 or 25 == let <= 30 or 35 == let <= 40 or 45 == let <= 50 or 55 == let <= 60 or 65 == let <= 70 or 75 == let <= 80 or 85 == let <= 90 or 95 == let <= 99:
        print('Мне', let, 'лет')
    else:
        print('Ага, столько не живут')
except (TypeError, ValueError):
    print('Вводи целыми, натуральными числами, а то не посчитаю')

