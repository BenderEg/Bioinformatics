import datetime

start = datetime.datetime.now()

with open(r'Salmonella enterica.txt', 'r') as fp:
    genome = fp.read()
    genome = genome.strip("\n")


def find_skew(genome):
    result = [0]
    count_C = 0
    count_G = 0
    for i in range(len(genome)):
        if genome[i] == 'C':
            count_C = count_C + 1
        if genome[i] == 'G':
            count_G = count_G + 1
        result.append(count_G - count_C)
    # result = ' '.join([str(elem) for elem in result])
    return result


def find_minimum(array):
    result = []
    minimum = min(array)
    for i in range(len(array)):
        if array[i] == minimum:
            result.append(i)
    result = ' '.join([str(elem) for elem in result])
    return result


def create_part_of_genome(genome, position, window):
    result = genome[position-window:position+window]
    return result


genome_changed = genome[400000:len(genome)] + genome[0:400000]
result = find_minimum(find_skew(genome_changed))
print(result)
output = create_part_of_genome(genome_changed, 3418639, 2000)


with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
    fp.write(output)

end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
