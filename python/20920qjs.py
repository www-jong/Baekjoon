from collections import deque
def bfs(node):
    visit=[[0]*(n+1) for i in range(n+1)]
    global count,level,exp
    q=deque()
    q.append(node)
    visit[node[0]][node[1]]=1
    fish={}
    short=10000
    while q:
        x,y=q.popleft()
        if graph[x][y]<level and graph[x][y]!=0:
            if visit[x][y]<=short:
                short=visit[x][y]
                if short in fish:
                    if fish[short][0]>x:
                        fish[short]=(x,y)
                    elif fish[short][0]==x and fish[short][1]>y:
                        fish[short]=(x,y) 
                else:
                    fish[short]=(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=n:
                if visit[nx][ny]==0 and graph[nx][ny]<=level:
                    visit[nx][ny]=visit[x][y]+1
                    q.append((nx,ny))
    min=10000
    if len(fish)!=0:
        for i in fish.keys():
            if i<min:
                min=i

        goeat=(fish[min])
        graph[fish[min][0]][fish[min][1]]=0
        count+=visit[fish[min][0]][fish[min][1]]-1
        exp+=1
        if exp==level:
            level+=1
            exp=0
        bfs(goeat)

n=int(input())
graph=[[0]*(n+1)]
level=2
exp=0
tmp=()
count=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    s=list(map(int,input().split()))
    s.insert(0,0)
    graph.append(s)
    if 9 in s:
        for j in range(len(s)):
            if s[j]==9:
                tmp=(i+1,j) 
graph[tmp[0]][tmp[1]]=0   
bfs(tmp)
print(count)