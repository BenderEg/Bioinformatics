# Finding frequent words by sorting

Text ='AAGCAAAGGTGGG'
k = 2    

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

def findingFrequentWordsBySorting(Text, k):     # функция для поиска наиболее часто встречающихся фрагментов заданной длинны (k) в тексе (Text)
    FrequentPatterns = []
    Index = []
    count = 1
    Count = []
    maxCount = 1
    
    for i in range(len(Text)-1):
        Pattern = Text[i:i+k]
        Index.append(patternToNumber(Pattern))
    Index.sort()

    for i in range(len(Index)):
        if Index[i] == Index[i-1]:
            count = count + 1
        else:
            count = 1
        Count.append(count)
        maxCount = max(Count)

    for i in range(len(Index)):
        if Count[i] == maxCount:
            FrequentPatterns.append(numberToPattern(Index[i], k))
    return FrequentPatterns

print(findingFrequentWordsBySorting(Text, k))
        
