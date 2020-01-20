#Genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

import datetime

start = datetime.datetime.now()

with open(r'C:\Users\Asus\Downloads\Input.txt', 'r') as fp:
    genome = fp.readline()
    genome = genome.strip('\n')

def find_skew(genome):
    result = [0]
    count_C = 0
    count_G = 0
    for i in range(len(genome)):
        if genome[i] == 'C':
            count_C = count_C + 1
        if genome[i] == 'G':
            count_G = count_G + 1
        result.append(count_G-count_C)
    #result = ' '.join([str(elem) for elem in result])
    return result

def find_minimum(array):
    result = []
    minimum = min(array)
    for i in range(len(array)):
        if array[i] == minimum:
            result.append(i)
    result = ' '.join([str(elem) for elem in result])
    return result

print(find_minimum(find_skew(genome)))

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
