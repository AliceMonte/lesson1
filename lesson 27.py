#Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
#Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.
def decorator(func):
    def wrapper(name):
        func(name.upper())
    return wrapper
@decorator
def hello(name):
    print('Привет,', name)
hello(input('Введите имя: '))