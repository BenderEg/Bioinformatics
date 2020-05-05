def create_data(file_name):
    stats = []
    for line in open(file_name):
        array = []
        for ele in line.strip().split(' '):
            if ele == '':
                break
            array.append(int(ele))
        stats.append(array)
    return stats


def create_adjacency_list_from_edges_list(array, V):
    adjacency_list = [[] for a in range(V)]
    for i in range(len(array)):
        number_1 = array[i][0]
        number_2 = array[i][1]
        if number_1 == number_2:
            adjacency_list[number_1].append(number_1)
        else:
            adjacency_list[number_1].append(number_2)
            adjacency_list[number_2].append(number_1)
    for i in range(len(adjacency_list)):
        adjacency_list[i].sort()
    return adjacency_list

array = create_data('Input.txt')
V = 10000
adjacency_list = create_adjacency_list_from_edges_list(array, V)
#print(adjacency_list)


def triangle(number):
    result = 0
    for a in adjacency_list[number]:
        if a != number:
            for b in adjacency_list[a]:
                if (b != number) and (b != a):
                    for c in adjacency_list[b]:
                        if c == number:
                            #print(number, a, b)
                            result += 1
    return result


count = 0
for k in range(V):
    if len(adjacency_list[k]) > 0:
       count += triangle(k)
print(count/6)