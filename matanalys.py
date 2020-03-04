def even(n):
    even = 1
    for i in range(2, n):
        if i % 2 == 0:
            even *= i
    return even

def uneven(n):
    uneven = 1
    for i in range(2, n):
        if i % 2 != 0:
            uneven *= i
    return uneven

x = []
for i in range(1, 5000):
    ele = i/(i**2+1)
    x.append(ele)
    print(ele)
    if ele > x[i - 2]:
        print('не монотонна')
else:
    print('монотонна')