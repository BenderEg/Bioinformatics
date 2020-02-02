import datetime

start = datetime.datetime.now()


def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats


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


def find_Hamming_distance(p, q):
    result = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            result += 1
    return result


array = create_data('Input.txt')

k = 5
d = 2

def implement_motif_enumeration(DNA, k, d):
    text = DNA[1]
    Patterns = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        neighbors = create_neighbors(pattern, d)
        for ele in neighbors:
            count = 0
            j = 2
            while j != len(DNA):
                j += 1
                search_text = DNA[j-1]
                for l in range(len(search_text)-k+1):
                    pattern_add = search_text[l:l+k]
                    if find_Hamming_distance(pattern_add, ele) <= d:
                        count += 1
                        break
            if count == len(DNA) - 2 and ele not in Patterns:
                Patterns.append(ele)
    output = ' '.join(Patterns)
    return output


output = implement_motif_enumeration(array, k, d)
with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
    fp.write(output)

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
