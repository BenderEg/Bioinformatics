# Solve the Pattern Matching Problem.

with open(r'C:\Users\Asus\Downloads\Input.txt', 'r') as fp: #открывает файл в режими "read only"
    Pattern = fp.readline()     # записывает содержимое первой строки в переменную
    Pattern = Pattern.strip('\n') # удаляет элемент в виде перехода на следующую строку
    Genome = fp.readline()      # записывает содержимое второй строки в переменную

maxValue = len(Genome)-len(Pattern)+1 # диапазон значений, просматриваемых в геноме (от 0 элемента до конца минус длина искомого фрагмента)

Result = [] # задает пустой лист

for i in range(maxValue):
    if Genome[i:i+len(Pattern)] == Pattern:
        Result.append(i) # добавляет к листу номер позиции, с которой начинается совпадение с искомым фрагментом

listToString = ' '.join([str(elem) for elem in Result])         #создает из списка строку с пробелами

with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:        # заполнение пустого файла результатом в формате строка
    fp.write(listToString)
