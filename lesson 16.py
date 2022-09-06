#1 Найти максимальный элемент диагонали матрицы.
n = int(input('Квадратный массив.Введите кол-во строк/столбцов:'))
A = []
for i in range(n):
    A1 = []
    for j in range(n):
        a = int(input('Введите число до 10: '))
        A1.append(a)
    A.append(A1)
for i in A:
    print('Наша квадратная матрица', i)
b = max(A[i][i] for i in range(int(len(A))))
print('Максимальный элемент диагонали матрицы: ', b)

#2 Вычислить количество отрицательных элементов под главной диагональю матрицы.
m = int(input('Квадратный массив.Введите кол-во строк/столбцов:'))
B = []
summ = 0
print('Наша квадратная матрица')
for i in range(m):
    B1 = []
    for j in range(m):
        c = int(input('Введите число до 10: '))
        B1.append(c)
    B.append(B1)
for i in B:
    print(i)
for i in range(m):
    for j in range(m):
        if i > j and B[i][j] < 0:
            summ += 1
print('Количество отрицательных элементов под главной диагональю матрицы: ', summ)

