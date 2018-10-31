prisoners = [False for __ in range(1000)]
for i in range(1, 1000):
    for j in range(0, 1000, i):
        prisoners[j] ^= True

s = list(i+1 for i, v in enumerate(prisoners) if v)
for i in s:
    print(i)
