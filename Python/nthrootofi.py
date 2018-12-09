def nthrootofi(i, n = 2, decimals = 8):
    prec = 10**-decimals
    def f(x):
        return x**n-i
    
    prev, curr = i / 10, i
    while abs(curr - prev) > prec:
        prev, curr = curr, prev - f(prev) / (n * prev**(n-1))
    return round(curr, decimals)

print(nthrootofi(2,3))
