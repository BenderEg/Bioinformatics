#p = 'GGGCCGTTGGT'
#q = 'GGACCGTTGAC'

import datetime

start = datetime.datetime.now()

def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats

def find_Hamming_distance(p,q):
    result = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            result += 1
    return result

print(find_Hamming_distance(create_data('Input.txt')[0], create_data('Input.txt')[1]))

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
