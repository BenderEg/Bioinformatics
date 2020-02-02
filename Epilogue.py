import datetime

start = datetime.datetime.now()


def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats


def find_Hamming_distance(p, q):
    result = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            result += 1
    return result


def create_neighborhood(pattern):
    result = []
    result.append(pattern)
    data = {'A': ['C', 'G', 'T'], 'C': ['A', 'G', 'T'], 'G': ['A', 'C', 'T'], 'T': ['A', 'C', 'G']}
    for element in pattern:
        for j in range(0, 3):
            neighbor = pattern.replace(element, data[element][j])
            result.append(neighbor)
    return result


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


def create_neighbors(pattern, d):
    output = ['A', 'C', 'G', 'T']
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return output
    neighbors = []
    first_symbol = pattern[0]
    suffix_pattern = pattern[1:]
    suffix_neighbors = create_neighbors(suffix_pattern, d)
    for ele in suffix_neighbors:
        if find_Hamming_distance(ele, suffix_pattern) < d:
            for elem in output:
                text = elem + ele
                neighbors.append(text)
        else:
            text = first_symbol + ele
            neighbors.append(text)
    return neighbors


def reverse_complement(text):
    reverse_complement = ''
    for i in range(len(text)):
        if text[i] == 'A':
            reverse_complement = 'T' + reverse_complement
        elif text[i] == 'T':
            reverse_complement = 'A' + reverse_complement
        elif text[i] == 'C':
            reverse_complement = 'G' + reverse_complement
        elif text[i] == 'G':
            reverse_complement = 'C' + reverse_complement
    return reverse_complement


def find_frequent_words_with_mismatches(genome, k, d, L):
    dict_1 = {a: 0 for a in range(4 ** k)}
    dict_2 = {a: [] for a in range(4 ** k)}
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k]
        neighbors = create_neighbors(pattern, d)
        for ele in neighbors:
            dict_1[patternToNumber(ele)] += 1
            dict_2[patternToNumber(ele)].append(i)
        reverse_pattern = reverse_complement(pattern)
        reverse_neighbors = create_neighbors(reverse_pattern, d)
        for ele in reverse_neighbors:
            if ele not in neighbors:
                dict_1[patternToNumber(ele)] += 1
                dict_2[patternToNumber(ele)].append(i)
    result_array = []
    for key in dict_2:
        if len(dict_2[key]) == 0:
            max_value = 0
        elif len(dict_2[key]) == 1:
            max_value = 1
        else:
            max_value = 1
            current_value = 1
            for i in range(1, len(dict_2[key])):
                if (L - k + 1) >= (dict_2[key][i] - dict_2[key][i-1]):
                    current_value += 1
                    max_value = current_value
                elif (L - k + 1) < (dict_2[key][i] - dict_2[key][i-1]):
                    current_value = 1
        result_array.append(max_value)
    max_value_in_dict_2 = max(result_array)
    result_without_check = []
    result = []
    while len(result) == 0:
        print(max_value_in_dict_2)
        for i in range(len(result_array)):
            if result_array[i] == max_value_in_dict_2:
                result_without_check.append(numberToPattern(i, k))
        for ele in result_without_check:
            for i in range(len(genome) - k + 1):
                pattern = genome[i:i + k]
                if pattern == ele and ele not in result and reverse_complement(ele) not in result:
                    result.append(ele)
        max_value_in_dict_2 += -1
    return result

genome = create_data('Input.txt')[0]
print(len(genome))
k = 9
d = 2

output = ' '.join(find_frequent_words_with_mismatches(genome, k, d, 500))
print(output)

# with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
    # fp.write(result)


end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)