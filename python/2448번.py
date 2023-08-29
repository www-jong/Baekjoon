N=int(input())
def func(x):
    res=[]
    if x==3:
        res=['  *  ',' * * ','*****']
        return res
    else:
        li=func(x//2)
        res=li[:]
        tmp=li[:]
        for i in range(x//2):
            tmp[i]+=' '+tmp[i]
        res+=tmp
        for i in range(x//2):
            res[i]=' '*(x//2)+res[i]+' '*(x//2)

        return res
li=func(N)
for i in range(N):
    print(li[i])