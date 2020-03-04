import datetime

start = datetime.datetime.now()


def create_data_special(file_name):
    stats = []
    str = ''
    for line in open(file_name):
        line = line.strip()
        if '>' not in line:
            str += line
        if '>' in line:
            stats.append(str)
            str = ''
    stats.append(str)
    stats.remove('')
    return stats


def create_data(file_name):
    stats = []
    for line in open(file_name):
        line = line.strip()
        stats.append(line)
    return stats


def count_symbols(text):
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for ele in text:
        if ele == 'A':
            d['A'] += 1
        if ele == 'C':
            d['C'] += 1
        if ele == 'G':
            d['G'] += 1
        if ele == 'T':
            d['T'] += 1
    output = []
    for ele in d:
        output.append(d[ele])
    output = ' '.join([str(elem) for elem in output])
    return output


def DNAtoRNA(text):
    result = []
    for ele in text:
        if ele == 'T':
            result.append('U')
        else:
            result.append(ele)
    output = ''.join([str(elem) for elem in result])
    return (output)


def reverse_complement(text):
    reverse_complement = ''
    for i in range(len(text)):
        if text[i] == 'A':
            reverse_complement = 'T' + reverse_complement
        elif text[i] == 'T':
            reverse_complement = 'A' + reverse_complement
        elif text[i] == 'C':
            reverse_complement = 'G' + reverse_complement
        elif text[i] == 'G':
            reverse_complement = 'C' + reverse_complement
    return reverse_complement


def rabbits(n, k):
    Rabbits = [1, 1]
    for i in range(2, n + 1):
        Rabbits.append(Rabbits[i - 2] * k + Rabbits[i - 1])
    return Rabbits[n - 1]


def count_GC(text):
    result = [0, 0]
    count = 0
    for ele in text:
        percent = 0
        if '>' not in ele:
            GC = 0
            for i in range(len(ele)):
                if ele[i] == 'G' or ele[i] == 'C':
                    GC += 1
            percent = round(GC / len(ele) * 100, 6)
        if percent > result[1] and count > 0:
            result[1] = percent
            result[0] = text[count - 1]
    count += 1
    return result


def find_Hamming_distance(p, q):
    result = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            result += 1
    return result


def create_protein(text):
    codon_table = {'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                   'AGA': 'R', 'AGG': 'R', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
                   'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'UUA': 'L', 'UUG': 'L',
                   'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
                   'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                   'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'AAU': 'N', 'AAC': 'N', 'GAU': 'D', 'GAC': 'D',
                   'UGU': 'C', 'UGC': 'C', 'CAA': 'Q', 'CAG': 'Q', 'GAA': 'E', 'GAG': 'E', 'CAU': 'H', 'CAC': 'H',
                   'AAA': 'K', 'AAG': 'K', 'UUU': 'F', 'UUC': 'F', 'UAU': 'Y', 'UAC': 'Y', 'AUG': 'M', 'UGG': 'W',
                   'UAG': '*', 'UGA': '*', 'UAA': '*'}
    protein = ''
    for j in range(0, len(text), 3):
        codon = text[j:j + 3]
        if codon_table[codon] == '*':
            break
        if codon in codon_table:
            protein = protein + codon_table[codon]
    return (protein)


def find_motif(text, pattern):
    locations = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            locations.append(i + 1)
    return locations


def calculate_protein_mass(text):
    d = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891,
         'I': 113.08406,
         'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858,
         'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
    protein_mass = 0
    for ele in text:
        if ele in d:
            protein_mass += d[ele]
    return round(protein_mass, 3)


def find_consensus(array):
    consensus_string = ''
    for i in range(len(array)):
        local_entropy = 0
        d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(len(array)):
            d[array[j][i]] += 1
        for ele in d:
            if d[ele] != 0:
                local_entropy += d[ele] / len(array) * math.log2(d[ele] / len(array))
        entropy -= local_entropy
    return entropy


def DNA_to_RNA(text):
    RNA = ''
    for ele in text:
        if ele == 'T':
            RNA += 'U'
        else:
            RNA += ele
    return RNA


def create_protein_with_open_frames(text):
    codon_table = {'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                   'AGA': 'R', 'AGG': 'R', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
                   'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'UUA': 'L', 'UUG': 'L',
                   'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
                   'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                   'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'AAU': 'N', 'AAC': 'N', 'GAU': 'D', 'GAC': 'D',
                   'UGU': 'C', 'UGC': 'C', 'CAA': 'Q', 'CAG': 'Q', 'GAA': 'E', 'GAG': 'E', 'CAU': 'H', 'CAC': 'H',
                   'AAA': 'K', 'AAG': 'K', 'UUU': 'F', 'UUC': 'F', 'UAU': 'Y', 'UAC': 'Y', 'AUG': 'M', 'UGG': 'W',
                   'UAG': '*', 'UGA': '*', 'UAA': '*'}
    proteins = []
    for i in range(3):
        protein = ''
        trigger = 0
        for j in range(i, len(text), 3):
            codon = text[j:j + 3]
            if codon == 'AUG':
                trigger = 1
            if codon in codon_table and codon_table[codon] == '*' and trigger == 1:
                if protein not in proteins and protein != '':
                    proteins.append(protein)
                trigger = 0
                protein = ''
            if codon in codon_table and trigger == 1:
                protein = protein + codon_table[codon]
    return proteins


def find_more_proteins(array):
    more_proteins = []
    for ele in array:
        for i in range(1, len(ele)):
            if ele[i] == 'M':
                more_proteins.append(ele[i:len(ele)])
    for ele in more_proteins:
        if ele not in array:
            array.append(ele)
    return array


def delete_intron(text, intron):
    for i in range(len(text) - len(intron) + 1):
        pattern = text[i:i + len(intron)]
        if pattern == intron:
            text = text.replace(pattern, '')
    return text


def transition_transvertion_ratio(text1, text2):
    transition = 0
    transvertion = 0
    for i in range(len(text1)):
        if text1[i] == 'A' and text2[i] == 'G':
            transition += 1
        if text1[i] == 'A' and (text2[i] == 'C' or text2[i] == 'T'):
            transvertion += 1
        if text1[i] == 'G' and text2[i] == 'A':
            transition += 1
        if text1[i] == 'G' and (text2[i] == 'C' or text2[i] == 'T'):
            transvertion += 1
        if text1[i] == 'T' and text2[i] == 'C':
            transition += 1
        if text1[i] == 'T' and (text2[i] == 'A' or text2[i] == 'G'):
            transvertion += 1
        if text1[i] == 'C' and text2[i] == 'T':
            transition += 1
        if text1[i] == 'C' and (text2[i] == 'A' or text2[i] == 'G'):
            transvertion += 1
    return round(transition / transvertion, 11)


def mortal_rabbits(n, m):
    Rabbits = [1, 1]
    month = 2
    while month < n:
        if month < m:
            Rabbits.append(Rabbits[-2] + Rabbits[-1])
        elif month == m:
            Rabbits.append(Rabbits[-2] + Rabbits[-1] - 1)
        else:
            Rabbits.append(Rabbits[-2] + Rabbits[-1] - Rabbits[-(m+1)])
        month += 1
    return Rabbits[- 1]


def mendels_first_low(k, m, n):
    sum = k + m + n
    result = round((4*(k*(k-1)+2*m*k+2*n*k+m*n)+3*m*(m-1))/(4*sum*(sum-1)), 5)
    return result


def calculate_E(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i**2)*2/(n*(n+1))
    return sum

def calculate_median(n):
    sum = 0
    return_sum = 0
    i = 1
    j = 1000
    while sum < 0.5:
        sum += i*2/(n*(n+1))
        return_sum += j * 2/(n*(n+1))
        i += 1
        j -= 1
    result = j
    return result

print(calculate_E(1000))
print(calculate_median(1000))

##with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
##fp.write(output)  


end = datetime.datetime.now()
elapsed_time = end - start
print(elapsed_time)
