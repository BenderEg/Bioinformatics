# Solve the Reverse Complement Problem

with open(r'C:\Users\Asus\Downloads\Input.txt', 'r') as fp: #открывает файл в режими "read only"
    Text = fp.readline()                # записывает содержимое строкой в переменную

Pattern = []            # создание пустого листа
j = ''                  # создание пустой строки

for i in range(len(Text)):          # цикл, проходящий по длинне переменной и заменяющий нуклеотиды на комплиментарные
    if Text[i] == 'A':
        j = 'T'
    elif Text[i] == 'T':
        j = 'A'
    elif Text[i] == 'C':
        j = 'G'
    elif Text[i] == 'G':
        j = 'C'  
    Pattern.append(j)           # добавление нуклеотидов в пустой лист

Pattern.reverse()               # обращение листа

def listToString(Pattern):      # создание функции, переводящей лист в строку без разделителей
    str = ''
    for ele in Pattern:
        str += ele
    return str

with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:        # заполнение пустого файла результатом работы функции в формате строка
    fp.write(listToString(Pattern))
