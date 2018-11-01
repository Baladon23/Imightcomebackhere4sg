def fancyprint(t):
    c = 2
    while c<=len(t):
        if t[c-2] != " ":
            print(t[:c-1])
        c+=1
    while c>=2:
        if t[c-2] != " ":
            print(t[:c-1])
        c-=1

fancyprint("Python is fun!!!")
