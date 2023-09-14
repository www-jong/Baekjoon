import sys
input=sys.stdin.readline
from collections import deque
N,L,R=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
d=[0,0,1,-1]
res=0

while True:
    check=0
    visit=[[0]*(N) for i in range(N)]
    graph=[]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                tmp=[]
                q=deque()
                q.append((i,j))
                visit[i][j]=1
                r=li[i][j]
                tmp.append((i,j))
                tot=1
                while q:
                    x,y=q.popleft()
                    for g in range(4):
                        nx,ny=x+d[g],y+d[3-g]
                        if 0<=nx<N and 0<=ny<N and L<=abs(li[x][y]-li[nx][ny])<=R and not visit[nx][ny]:
                            #print(abs(li[x][y]-li[nx][ny]))
                            tmp.append((nx,ny))
                            visit[nx][ny]=1
                            r+=li[nx][ny]
                            tot+=1
                            check=1
                            q.append((nx,ny))
                tmp.append(r)
                tmp.append(tot)
                graph.append(tmp)
    for tmp in graph:
        tot=tmp.pop()
        r=tmp.pop()
        for x,y in tmp:
            li[x][y]=r//tot

    if not check:
        break
    #print(graph)
    #for i in li:
    #    print(i)
    #print('-__')
    res+=1
print(res)