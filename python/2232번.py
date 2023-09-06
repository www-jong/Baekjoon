import sys
imput=sys.stdin.readline
N=int(input())
li=[[int(input()),i] for i in range(N)]
t=sorted(li)
bombs=set()
res=[]
while len(bombs)!=N:
    power,idx=t.pop()
    if idx in bombs:
        continue
    res.append(idx+1)
    bombs.add(idx)
    didx,uidx=idx,idx
    dp,up=power,power
    while True:
        if uidx+1>=N or li[uidx+1][0]>=up or uidx+1 in bombs:
            break
        uidx+=1
        bombs.add(uidx)
        up=li[uidx][0]
    while True:
        if didx-1<0 or li[didx-1][0]>=dp or didx-1 in bombs:
            break
        didx-=1
        bombs.add(didx)
        dp=li[didx][0]
print(*sorted(res),sep='\n')