def create_data(file_name):
    stats = []
    for line in open(file_name):
        stats.append(line.strip().split(' '))
    return stats


data = create_data('Input.txt')
print(data)