def func(tmp,idx):
    if idx==M:
        print(*tmp)
        return
    for i in li:
        if tmp and tmp[-1]<=i:
            func(tmp+[i],idx+1)
        elif not tmp:
            func(tmp+[i],idx+1)
N,M=map(int,input().split())
li=list(set([*map(int,input().split())]))
li.sort()
func([],0)