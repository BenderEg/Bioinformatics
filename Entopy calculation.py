import datetime
import math

start = datetime.datetime.now()


def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats


def create_data_special(file_name):
    stats = []
    str = ''
    for line in open(file_name):
        line = line.strip()
        if '>' not in line:
            str += line
        if '>' in line:
            stats.append(str)
            str = ''
    stats.append(str)
    stats.remove('')
    return stats


def entropy_calculation(array):
    entropy = 0
    for i in range(len(array[0])):
        local_entropy = 0
        d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(len(array)):
            d[array[j][i]] += 1
        for ele in d:
            if d[ele] != 0:
                local_entropy += d[ele] / len(array) * math.log2(d[ele] / len(array))
        entropy -= local_entropy
    return entropy


def find_Hamming_distance(p, q):
    result = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            result += 1
    return result


def motifs_determination(Pattern, DNA):
    motifs = [0 for i in range(len(DNA))]
    DNA_number = 0
    for ele in DNA:
        local_min = len(Pattern)
        for i in range(len(ele) - len(Pattern) + 1):
            text = ele[i:i + len(Pattern)]
            d = find_Hamming_distance(text, Pattern)
            if d < local_min:
                motifs[DNA_number] = text
                local_min = d
        DNA_number += 1
    return motifs


def distance_determination(Pattern, DNA):
    distance = 0
    DNA_number = 0
    for ele in DNA:
        local_min = len(Pattern)
        for i in range(len(ele) - len(Pattern) + 1):
            text = ele[i:i + len(Pattern)]
            d = find_Hamming_distance(text, Pattern)
            if d < local_min:
                local_min = d
        distance += local_min
    return distance


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


def min_distance_determination(Pattern, DNA):
    distance = 0
    DNA_number = 0
    for ele in DNA:
        local_min = len(Pattern)
        for i in range(len(ele) - len(Pattern) + 1):
            text = ele[i:i + len(Pattern)]
            if text == Pattern:
                distance += 1
                break
    return distance


def patternToNumber(pattern):
    d = {'A':0, 'C':1, 'G':2, 'T':3}
    array = []
    for ele in pattern:
        array.append(d[ele])
    x = len(array)
    Number = 0
    i = 0
    while x != 0:
        Number += array[i]*(4**(x-1))
        x += - 1
        i += + 1
    return Number

def median_string_determination(k, DNA, patterns):
    median_string = 0
    distance = len(DNA) * k
    for ele in patterns:
        d = min_distance_determination(ele, DNA)
        if d == len(DNA):
            median_string = ele
            break
    return median_string

def create_patterns (text, k):
    patterns = []
    for i in range(len(text)-k+1):
        pattern = text[i:i + k]
        if pattern not in patterns:
            patterns.append(pattern)
    return patterns


def create_patterns_by_adding(pattern):
    patterns = []
    patterns.append(pattern + 'A')
    patterns.append(pattern + 'C')
    patterns.append(pattern + 'G')
    patterns.append(pattern + 'T')
    return patterns


k = 10
DNA = create_data_special('Input.txt')
patterns = create_patterns(DNA[0], k)
x = ''

while x != 0:
    x = median_string_determination(k, DNA, patterns)
    print(x, k)
    k += 1
    patterns = create_patterns_by_adding(x)

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
