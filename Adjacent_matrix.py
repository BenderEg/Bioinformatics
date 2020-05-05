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


def create_adjacency_list_from_adjacent_matrix(array, V):
    adjacency_list = [[] for a in range(V)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            m = 1
            while m <= array[i][j]:
                adjacency_list[i].append(j)
                m += 1
    for k in range(len(adjacency_list)):
        adjacency_list[k].sort()
    return adjacency_list


def even_check_for_V(array):
    for i in range(len(array)):
        sum = 0
        count = 0
        for j in range(len(array[i])):
            if array[i][j] == i:
                count += 1
        sum = len(array[i])+count
        if sum%2 != 0:
            return 'No'
    return 'Yes'


array = create_data('Input.txt')
V = int(array[0][0])
visited = [False] * V
array.remove(array[0])
print(array)
adjacency_list = create_adjacency_list_from_adjacent_matrix(array, V)
print(adjacency_list)

print(even_check_for_V(adjacency_list))