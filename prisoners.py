prisoners = [False for __ in range(1000)]
for i in range(1, 1001):
    for j in range(i-1, 1000, i):
        prisoners[j] = not prisoners[j]

[print(i) for i in list(i+1 for i, v in enumerate(prisoners) if v)]
