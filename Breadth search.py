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


def create_data_from_input(x):
    stats = []
    for line in x:
        array = []
        for ele in line.strip().split(' '):
            if ele == '':
                break
            array.append(int(ele))
        stats.append(array)
    return stats

x = input().strip().split(' ')
def create_data_from_input(value):
    n = 0
    stats = []
    for i in range(value):
        line = input()
        array = []
        for ele in line.strip().split(' '):
            array.append(int(ele))
        stats.append(array)
    return stats

array = create_data_from_input(int(x[1]))
V = int(x[0])
visited = [False] * V
adjacency_list = create_adjacency_list_from_edges_list(array, V)
#array = create_data('Input.txt')
#V = int(array[0][0])
#visited = [False] * V
#array.remove(array[0])
#djacency_list = create_adjacency_list_from_edges_list(array, V)
#print(adjacency_list)

def breadth_search(array, number, V, visited):
    Queue = []
    visited[number] = True
    Queue.insert(0, number)
    root = [0] * V
    count = 0
    while len(Queue) != 0:
        x = Queue.pop()
        if x == -1:
            count += 1
        else:
            if x != 0:
               root[x] = count
            for ele in array[x]:
                if -1 not in Queue:
                    Queue.insert(0, -1)
                if not visited[ele]:
                    Queue.insert(0, ele)
                    visited[ele] = True
    result = ' '.join([str(ele) for ele in root])
    return result


def breadth_search_bipartite(array, number, V, visited):
    Queue = []
    visited[number] = True
    Queue.insert(0, number)
    root = [0] * V
    count = 0
    while len(Queue) != 0:
        x = Queue.pop()
        if x == -1:
            count += 1
        else:
            if x != 0:
                root[x] = count
            for ele in array[x]:
                if -1 not in Queue:
                    Queue.insert(0, -1)
                if not visited[ele]:
                    Queue.insert(0, ele)
                    visited[ele] = True
    result = ' '.join([str(ele) for ele in root])
    return result

print(breadth_search(adjacency_list, 0, V, visited))