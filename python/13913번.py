from collections import deque
N,K=map(int,input().split())
li=[0]*(100001)
move=[0]*(100001)
res=[]
q=deque()
q.append(N)
while q:
    x=q.popleft()
    if x==K:
        print(li[x])
        break
    for i in (x-1,x+1,2*x):
        if 0<=i<=100000 and li[i]==0:
            li[i]=li[x]+1
            q.append(i)
            move[i]=x

res=[K]
x=K
while x!=N:
    res.append(move[x])
    x=move[x]
print(*res[::-1])