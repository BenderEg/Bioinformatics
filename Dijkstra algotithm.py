class BinHeap():
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i][1] < self.heaplist[i // 2][1]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, V, meanValue):
        couple = (V, meanValue)
        self.heaplist.append(couple)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percDown(self, i):
        while (i * 2) <= self.currentsize:
            mc = self.minChild(i)
            if self.heaplist[i][1] > self.heaplist[mc][1]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2][1] < self.heaplist[i * 2 + 1][1]:
                return i * 2
            else:
                return i * 2 + 1

    def deleteMin(self):
        retValue = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retValue

    def printHeap(self):
        return self.heaplist

    def calclength(self):
        return self.currentsize

    def findValue(self, V):
        i = 0
        while i < self.currentsize:
            i += 1
            if self.heaplist[i][0] == V:
                return self.heaplist[i][1]

    def changeValue(self, V, value):
        i = 0
        while i < self.currentsize:
            i += 1
            if self.heaplist[i][0] == V:
                self.heaplist[i] = (V, value)
                break
        self.percUp(i)

def create_data(file_name):
    stats = []
    """массив, содержащий список смежности"""
    for line in open(file_name):
        array = []
        """создает элемент будующего массива"""
        for ele in line.strip().split(' '):
            """убирает лишние пробелы"""
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
            adjacency_list[number_1].append([number_1, array[i][2]])
        else:
            adjacency_list[number_1].append([number_2, array[i][2]])
            adjacency_list[number_2].append([number_1, array[i][2]])
    for i in range(len(adjacency_list)):
        adjacency_list[i].sort()
    return adjacency_list

array = create_data('Input.txt')
V = int(array[0][0])
array.remove(array[0])
adjacency_list = create_adjacency_list_from_edges_list(array, V)

def algorihtmDijkstra(array, V, N):
    stack = BinHeap()
    stack.insert(N, 0)
    visited = [False] * V
    distance = [float('inf')] * V
    while stack.calclength() > 0:
        tmp = stack.deleteMin()
        visited[tmp[0]] = True
        distance[tmp[0]] = tmp[1]
        for ele in array[tmp[0]]:
            if not visited[ele[0]]:
                tmp_stack_value = stack.findValue(ele[0])
                if tmp_stack_value == None:
                    stack.insert(ele[0], ele[1] + tmp[1])
                    distance[ele[0]] = ele[1] + tmp[1]
                else:
                    tmp_insert_value = tmp[1] + ele[1]
                    if tmp_stack_value > tmp_insert_value:
                        stack.changeValue(ele[0], tmp_insert_value)
                        distance[ele[0]] = tmp_insert_value
    return distance

x = algorihtmDijkstra(adjacency_list, V, 0)
print(x)