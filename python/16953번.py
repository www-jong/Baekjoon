from collections import deque
a,b=map(int,input().split())
visit={}
q=deque()
q.append(a)
visit[a]=1
while q:
    n=q.popleft()
    if n==b:
        break    
    if n*2<=b: 
        if n*2 not in visit:
            visit[n*2]=visit[n]+1
        elif visit[n*2]>visit[n]+1:
            visit[n*2]=visit[n]+1
        q.append(n*2)
    g=int(str(n)+"1")
    if g<=b:
        if g not in visit:
            visit[g]=visit[n]+1
        if visit[g]>visit[n]+1:
            visit[g]=visit[n]+1
        q.append(g)
print(visit[b] if b in visit else -1)