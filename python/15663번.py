def func(tmp,x):
    global check
    if len(tmp)==M:
        if tmp not in check:
            check[tmp]=1
            print(*tmp)
        return
    for i in range(len(li)):
        if i not in x:
            func(tmp+(li[i],),x.union({i}))
N,M=map(int,input().split())
li=sorted(list(map(int,input().split())))
check={}
func((),{-1})
