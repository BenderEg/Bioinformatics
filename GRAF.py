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


array = create_data('Input.txt')
visited = [False]*int(array[0][0])
array.remove(array[0])


def dfs(number):
    visited[number] = True
    for ele in array[number]:
        if not visited[ele]:
            dfs(ele)
    return visited.count(True)

print(dfs(0))