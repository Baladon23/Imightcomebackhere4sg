#lsec mint longest section; mindig agyament fgvneveket eszelek ki
def lsec(a, b, c, l):
    if a == 0:
        return c
    while a < b:
        a *= 10
        c += 1
    if a%b in l:
        return c
    return lsec(a%b, b, c+1, l+[a%b])
            
maxx, maxi, a = 0, 0, 1
for i in range(1,1001):
    a = lsec(1, i, 0, [])
    if a > maxx:
      maxx = a
      maxi = i

print(maxi)
