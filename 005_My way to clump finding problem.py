import datetime

start = datetime.datetime.now()

with open(r'C:\Users\Asus\Downloads\Input.txt', 'r') as fp:
    genome = fp.readline()
    genome = genome.strip('\n')

k = 9
L = 500
t = 3


def numberToPattern(index,
                    k):  # создание функции, переводящей индекс при определенном k в последовательность нуклеотидов
    k_mer_list = []  # содание пустого листа
    k_mer_ACGT = []  # содание пустого листа
    fractional_part = index  # исходный индекс присваивается переменной
    reminder = 0  # в эту переменную записывается остаток от деления
    k_mer = ''  # создание пустой строки
    d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    while fractional_part >= 4:  # цикл, пока целое отделения не будет меньше 3
        reminder = fractional_part % 4  # остаток от опередации деления на 4
        fractional_part = fractional_part // 4  # целое от опередации деления на 4
        k_mer_list.insert(0, reminder)  # добавление в начало листа остатка от деления
    k_mer_list.insert(0, fractional_part)  # добавление в начало листа целого от последеней операции деления
    while len(
            k_mer_list) < k:  # цикл добавляющий нули в начало листа пока количество элементов в листе не будет соответствовать длине k
        k_mer_list.insert(0, 0)
    for ele in k_mer_list:  # переход от числового листа к буквенному
        k_mer = k_mer + d[ele]
    return k_mer


def patternToNumber(pattern):  # функция дле перевод буквенной строки нуклеотидов в числовой индекс
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    array = []
    for ele in pattern:
        array.append(d[ele])
    x = len(array)
    Number = 0
    i = 0
    while x != 0:
        Number += array[i] * (4 ** (x - 1))
        x += - 1
        i += + 1
    return Number


def ClumpFinding(genome, k, L, t):
    d = {a: [] for a in range(4 ** k)}
    for i in range(len(genome) - k + 1):
        row = genome[i:i + k]
        d[patternToNumber(row)].append(i)
    result_array = []
    for i in d:
        if len(d[i]) >= t:
            for j in range(len(d[i]) - t + 1):
                if (d[i][j + t - 1] + k) - d[i][j] <= L:
                    result_array.append(numberToPattern(i, k))
                    break
    return str(len(result_array))


print(ClumpFinding(genome, k, L, t))

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
