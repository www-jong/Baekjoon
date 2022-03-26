from collections import deque
n=int(input())
graph=[[0]]
maxdeep=0
for i in range(n):
    asd=list(map(int,input().split()))
    if maxdeep<max(asd):
        maxdeep=max(asd)
    graph.append([0]+asd)
ans=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for dd in range(0,maxdeep):
    count=0
    visit=[[0]*(n+1) for i in range(n+1)]
    for aa in range(1,n+1):
        for bb in range(1,n+1):
            q=deque()
            if graph[aa][bb]>dd and visit[aa][bb]==0:
                visit[aa][bb]=1
                q.append((aa,bb))
                count+=1
            else:continue
            while q:
                x,y=q.popleft()
                for i in range(4):
                    sx=x+dx[i]
                    sy=y+dy[i]
                    if 0<sx<=n and 0<sy<=n:
                        if graph[sx][sy]>dd and visit[sx][sy]==0:
                            q.append((sx,sy))
                            visit[sx][sy]=1     
    ans.append(count)
print(max(ans))
                