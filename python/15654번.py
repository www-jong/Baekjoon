N,M=map(int,input().split())
li=list(map(int,input().split()))
li.sort()

def func(lis):
    if len(lis)==M:
        print(*lis,sep=" ")
        return
    for i in range(N):
        if li[i] not in lis:
            func(lis+[li[i]])
func([])
