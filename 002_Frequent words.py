# the frequent words problem

Text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
k = 3
maxValue = len(Text) - k + 1
Patterns = []
Counts = []

for i in range(maxValue):
    Pattern = Text[i:i+k]
    Patterns.append(Pattern)

for i in Patterns:
    value = Patterns.count(i)
    Counts.append(value)

Y = []
for i in range(maxValue):
    if Counts[i] == max(Counts):
        Y.append(Patterns[i])

Y.sort()
      
print (list(set(Y)))
