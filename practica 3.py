#1
k = 11
print('Числа кратные 11: ')
for i in range(0, 10000+1):
    if i % k == 0:
        if i > 0:
            print(i)
