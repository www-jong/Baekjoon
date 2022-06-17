from collections import deque
n=int(input())
visit=[[10**9,[]] for i in range(n+1)]
q=deque()
q.append((n,0))
while q:
    x,y=q.popleft()
    if x==1:
        visit[1][1]+=[1]
        print(visit[1][0] if visit[1][0]<10**8 else 0)
        print(*visit[1][1])
        break
    if x%3==0 and visit[x//3][0]>y:
        q.append((x//3,y+1))
        visit[x//3][0]=y+1
        visit[x//3][1]=visit[x][1]+[x]
    if x%2==0 and visit[x//2][0]>y:
        q.append((x//2,y+1))
        visit[x//2][0]=y+1
        visit[x//2][1]=visit[x][1]+[x]
    if visit[x-1][0]>y:
        q.append((x-1,y+1))
        visit[x-1][0]=y+1
        visit[x-1][1]=visit[x][1]+[x]
