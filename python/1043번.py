N,M=map(int,input().split())
t=list(map(int,input().split()))
if len(t)>=2:
    t=set(t[1:])
else:
    t=set()
li=[]
tmp=[]
plag=0
for i in range(M):
    li.append(list(map(int,input().split()))[1:])
for i in range(M-1,-1,-1):
    g=set(li[i])
    if t:
        if t&g:
            t=t.union(g)
        else:
            tmp.append(g)
    else:
        plag=1
        break
check=1
idx=0

if plag==0:
    while idx<len(tmp):
        if t&tmp[idx]:
            t=t.union(tmp[idx])
            tmp=tmp[:idx]+tmp[idx+1:]
            idx=0
        else:
            idx+=1
    print(len(tmp))
else:
    print(M)
print(tmp)
print(t)