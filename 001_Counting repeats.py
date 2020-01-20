## finding a pattern in the text

Text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'
Pattern = 'CGCG'

maxValue = len(Text)-len(Pattern) # максимально возможное значение, до которого идет подсчет
count = 0 #задает переменную

for i in range(maxValue): # задает диапазон для i
    if Text[i:i+len(Pattern)] == Pattern: # выделяет фрагмент в последовательности и сравнивает его с заданным
        count = count + 1 # добавляет к переменной 1 при совпадении

print(count)


