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
        number_1 = array[i][0]-1
        number_2 = array[i][1]-1
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
#array = create_data('Input.txt')
#V = int(array[0][0])
#array.remove(array[0])
visited = [False] * V
adjacency_list = create_adjacency_list_from_edges_list(array, V)


def dfs(number):
    visited[number] = True
    for ele in adjacency_list[number]:
        if not visited[ele]:
            dfs(ele)
    return visited.count(True)


# count = 0
# for k in range(V):
# if not visited[k]:
# dfs(k)
# count += 1
# print(count)


def deep_search(array, number, visited):
    stack = []
    stack.append(number)
    visited[number] = True
    while len(stack) != 0:
        x = stack.pop(0)
        for ele in array[x]:
            if not visited[ele]:
                stack.append(ele)
                visited[ele] = True
    return visited.count(True)


count = 0
for k in range(V):
    if not visited[k]:
       deep_search(adjacency_list, k, visited)
       count += 1
print(count)
