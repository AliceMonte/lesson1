try:
    print('Вводите целые числа от 1')
    year1 = int(input('Аня родилась в году: '))
    month1 = int(input('в месяце: '))
    date1 = int(input('числа: '))
    year2 = int(input('Катя родилась в году: '))
    month2 = int(input('в месяце: '))
    date2 = int(input('числа: '))
    print('Сегодня:')
    year_t = int(input('год '))
    month_t = int(input('месяц '))
    date_t = int(input('число '))
    if 0 < month1 <= 12 and 0 < month2 <= 12 and 0 < month_t <= 12:
        let1 = ((int(year_t) - int(year1)) * 12 + int(month_t) - int(month1)) // 12
        let2 = ((int(year_t) - int(year2)) * 12 + int(month_t) - int(month2)) // 12
        print('Ане', let1)
        print('Кате', let2)
        if let1 < let2:
            print('Аня младше Кати')
        else:
            print('Катя младше Ани')
    else:
        print('В году не больше 12 месяцев, в месяце не больше 31 дня')

except (TypeError, ValueError):
    print('Вводи целыми, натуральными числами, а то не посчитаю')