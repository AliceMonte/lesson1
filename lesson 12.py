#1
x = int(input("Введите число:"))
m = 0
while (x):
    if (x % 10 > m):
        m = x % 10
    x //= 10
print(m)

#1.2
n = input("Введите число:")
b = len(n)
n = int(n)
Arr = []
for i in range(b):
    c = n % 10
    Arr.append(c)
    n = n // 10
print(c)

#2
a = str(input("Введите число:"))
print(a[::-1])