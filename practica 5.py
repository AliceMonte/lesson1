#В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество символов и слов в ней.
f = open('text1.txt', encoding='utf8')
line = 0
for i in f:
    line += 1
    flag = 'вне слова'
    word = 0
    for j in i:
        if j != ' ' and flag == 'вне слова':
            word += 1
            flag = 'в слове'
        elif j == ' ':
            flag = 'вне слова'
    print(i,len(i),'символов',word,'слов')
print('В тексте',line,'строк.')
f.close()