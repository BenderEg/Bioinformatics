import datetime
import math

start = datetime.datetime.now()


def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats


array = create_data('Input.txt')


def entropy_calculation(array):
    entropy = 0
    for i in range(len(array[0])):
        local_entropy = 0
        d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(len(array)):
            d[array[j][i]] += 1
        for ele in d:
            if d[ele] != 0:
                local_entropy += d[ele]/len(array)*math.log2(d[ele]/len(array))
        print(local_entropy)
        entropy -= local_entropy
    return entropy


print(entropy_calculation(array))

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)