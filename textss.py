def fancyprint(t):
    c = 2
    while c<=len(t):
        print(t[:c-1])
        c+=1
    while c>=2:
        print(t[:c-1])
        c-=1

fancyprint("Beletelt vagy tíz percbe, de ez nagyon király.")
