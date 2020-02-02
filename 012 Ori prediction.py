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


def find_pattern(pattern, text, d):
    result = []
    for i in range(len(text) - len(pattern) + 1):
        part = text[i:i + len(pattern)]
        if find_Hamming_distance(part, pattern) <= d:
            result.append(i)
    return len(result)


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


def find_frequent_words_with_mismatches(genome, k, d):
    dict_1 = {a: 0 for a in range(4 ** k)}
    dict_2 = {a: [] for a in range(4 ** k)}
    result_array = []
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k]
        neighbors = create_neighbors(pattern, d)
        for ele in neighbors:
            dict_1[patternToNumber(ele)] += 1
            dict_2[patternToNumber(ele)].append(i)
        reverse_pattern = reverse_complement(pattern)
        reverse_neighbors = create_neighbors(reverse_pattern, d)
        for ele in reverse_neighbors:
            dict_1[patternToNumber(ele)] += 1
            dict_2[patternToNumber(ele)].append(i)
    result_array = [key for m in [max(dict_1.values())] for key, val in dict_1.items() if val == m]
    result = []
    for ele in result_array:
        result.append(numberToPattern(ele, k))
    result_array_with_pattern_really_appear = []
    for ele in result:
        for i in range(len(genome) - k + 1):
            pattern = genome[i:i + k]
            if (pattern == ele and ele not in result_array_with_pattern_really_appear and reverse_complement(ele)
                    not in result_array_with_pattern_really_appear):
                result_array_with_pattern_really_appear.append(ele)
                ##  result_array_with_pattern_really_appear.append(reverse_complement(ele))
    output = ' '.join(result_array_with_pattern_really_appear)
    return output


def find_frequent_words_with_mismatches_additional(genome, k, d):
    dict = {a: 0 for a in range(4 ** k)}
    result_array = []
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i + k]
        neighbors = create_neighbors(pattern, d)
        for ele in neighbors:
            dict[patternToNumber(ele)] += 1
        reverse_pattern = reverse_complement(pattern)
        reverse_neighbors = create_neighbors(reverse_pattern, d)
        for ele in reverse_neighbors:
            dict[patternToNumber(ele)] += 1
    max_value = max(dict.values())
    return max_value

genome = create_data('Input.txt')[0]
k = 9
d = 2


def find_max_starting_positions(text, k, d, L):
    array_with_max = []
    for i in range(len(text)-L):
        genome = text[i:i+L]
        array_with_max.append(find_frequent_words_with_mismatches_additional(genome, k, d))
    max_value = max(array_with_max)
    result_array = []
    for i in range(len(array_with_max)):
        if array_with_max[i] == max_value:
            result_array.append(i)
    return result_array


# result = find_max_starting_positions(genome, k, d, 500)
# print(result)
genome_final_part = genome[400:900]
result = find_frequent_words_with_mismatches(genome, k, d)
print(result)

# with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
    # fp.write(result_string)

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)