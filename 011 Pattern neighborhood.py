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

def create_neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        output = ['A', 'C', 'G', 'T']
        return output

print(create_neighbors('A', 1))
print('Hello')


output = create_neighborhood(create_data('Input.txt')[0])
print(output)

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
