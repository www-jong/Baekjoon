li=[(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1),(3,3,2),(3,3,3),(2,3,3),(3,2,3)]

for a,b,c in li:
    if a>=b:
        if a>=c:
            print(a)
        else:
            print(c)
    else:
        if b>=c:
            print(b)
        else:
            print(c)
