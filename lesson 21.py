# В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
f = 'spisok.txt'
with open(f, encoding='utf8') as content:
    content = content.read()
content = content.split("\n")
students = []
for line in content:
    line = line.split(" ")
    students.append([line[0], line[1], int(line[2])])
sr = 0
print("Ниже 3 баллов:")
for s in students:
    sr += int(s[2])
    if s[2] < 3:
        print(f"{s[0]} {s[1]}: {s[2]}")
sr/= len(students)
print(f"Средняя оценка по классу: {sr}")

#Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
filename = 'text.txt'
f = open(filename,'w')
i = 0
while True:
    s = input('Введите строку '+str(i+1)+': ')
    i += 1
    if s == '': break
    f.write(s+'\n')
f.close()
with open(filename, 'r') as file:
    for s in file:
        print(s, end='')