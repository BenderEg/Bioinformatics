# Finding frequent words by sorting

import datetime

start = datetime.datetime.now()

with open(r'C:\Users\Asus\Downloads\Input.txt', 'r') as fp:
    Genome = fp.readline()
    Genome = Genome.strip('\n')

#Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'

k = 9
L = 500
t = 3

print(len(Genome))

def numberToPattern(index,k):       #создание функции, переводящей индекс при определенном k в последовательность нуклеотидов
    k_mer = []      # содание пустого листа
    k_mer_ACGT = [] # содание пустого листа
    fractional_part = index     #исходный индекс присваивается переменной
    reminder = 0            #в эту переменную записывается остаток от деления
    while fractional_part >= 4:     #цикл, пока целое отделения не будет меньше 3
        reminder = fractional_part%4    #остаток от опередации деления на 4
        fractional_part = fractional_part//4    #целое от опередации деления на 4
        k_mer.insert(0,reminder)    #добавление в начало листа остатка от деления
    k_mer.insert(0,fractional_part) #добавление в начало листа целого от последеней операции деления
    while len(k_mer)<k:     # цикл добавляющий нули в начало листа пока количество элементов в листе не будет соответствовать длине k
        k_mer.insert(0,0)
    for ele in k_mer:       #переход от числового листа к буквенному
        if ele == 0:
            k_mer_ACGT.append('A')
        if ele == 1:
            k_mer_ACGT.append('C')
        if ele == 2:
            k_mer_ACGT.append('G')
        if ele == 3:
            k_mer_ACGT.append('T')
    k_mer = ''      #создание пустой строки
    for ele in k_mer_ACGT: 
        k_mer += ele        #перевод листа в строку
    return k_mer
    
def patternToNumber (pattern):      # функция дле перевод буквенной строки нуклеотидов в числовой индекс
    array = []
    for ele in pattern:
        if ele == 'A':
            array.append(0)
        if ele == 'C':
            array.append(1)
        if ele == 'G':
            array.append(2)
        if ele == 'T':
            array.append(3)
    x = len(array)
    Number = 0
    i = 0
    while x != 0:
        Number += array[i]*(4**(x-1))
        x += - 1
        i += + 1
    return Number

def computingFrequencies(Text,k):
    FrequencyArray = []
    j = 0
    Output = ''
    for i in range(4**k):
        FrequencyArray.append(0)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        j = patternToNumber(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray
    
def clumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    FrequencyArray = []
    Clump = []
    Text = Genome[0:L]
    FirstPattern = ''
    LastPattern = ''
    index = 0
    
    for i in range(4**k):
        Clump.insert(0,0)
        
    FrequencyArray = computingFrequencies(Text,k)
    
    for i in range(4**k):
        if FrequencyArray[i] == t:
            Clump[i] = 1  
    for i in range(1, len(Genome)-L):
        FirstPattern = Genome[i-1:k]
        index = patternToNumber(FirstPattern)
        FrequencyArray[index] = FrequencyArray[index] - 1
        LastPattern = Genome[(i+L-k-1):(i+L-1)]
        index = patternToNumber(LastPattern)
        FrequencyArray[index] = FrequencyArray[index] + 1
        if FrequencyArray[index] == t:
            Clump[index] = 1
    for i in range(4**k):   
        if Clump[i] == 1:
            FrequentPatterns.append(numberToPattern(i,k))
    #stringFrequentPatterns = ' '.join([str(elem) for elem in FrequentPatterns])
    output = str(len(FrequentPatterns))
    return output

with open(r'C:\Users\Asus\Downloads\Output.txt', 'w') as fp:
     fp.write(clumpFinding(Genome, k, L, t))

end = datetime.datetime.now()

elapsed_time = end - start
print(elapsed_time)
