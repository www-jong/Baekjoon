from collections import deque
N,M=map(int,input().split())
#maps=[i for i in range(1,102)]
maps=[0]*(101)
visit=[0]*(101)
for i in range(N):
    a,b=map(int,input().split())
    maps[a]=b
for i in range(M):
    a,b=map(int,input().split())
    maps[a]=b
count=1000000
q=deque()
q.append((1,0))
visit[1]=1
while q:
    x,co=q.popleft()
    for i in range(1,7):
        nx=i+x
        if 1<=nx<=100:
            if not visit[nx]:
                if nx==100:
                    count=min(count,co+1)
                if maps[nx]==0:
                    q.append((nx,co+1))
                    visit[nx]=1
                else:
                    q.append((maps[nx],co+1))
                    visit[nx],visit[maps[nx]]=1,1
print(count)