# Solve the Pattern Matching Problem.

with open(r'C:\Users\Asus\Downloads\Vibrio_cholerae.txt', 'r') as fp: #открывает файл в режими "read only"
    Pattern = 'CTTGATCAT'       
    Genome = fp.readline()          # записывает содержимое строкой в переменную

maxValue = len(Genome)-len(Pattern) # диапазон значений, просматриваемых в геноме (от 0 элемента до конца минус длина искомого фрагмента)

Result = [] # задает пустой лист

for i in range(maxValue):
    if Genome[i:i+len(Pattern)] == Pattern:
        Result.append(i) # добавляет к листу позицию, с которой начинается совпадение с искомым фрагментом)

listToString = ' '.join([str(elem) for elem in Result])     # создает строку с пробелами из листа

with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:        # заполнение пустого файла результатом в формате строка
    fp.write(listToString)
