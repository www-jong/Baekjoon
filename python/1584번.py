from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

li=[[0]*(501) for _ in range(501)]
den=[]
death=[]
N=int(input())
for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())
    den.append((x1,y1,x2,y2))

M=int(input())
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    death.append((x1,y1,x2,y2))

for x1,y1,x2,y2 in den:
    x1,x2=min(x1,x2),max(x1,x2)
    y1,y2=min(y1,y2),max(y1,y2)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            li[i][j]=1

for x1,y1,x2,y2 in death:
    x1,x2=min(x1,x2),max(x1,x2)
    y1,y2=min(y1,y2),max(y1,y2)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            li[i][j]=2

res=0
visit=[[0]*(501) for i in range(501)]
q=deque()
q.append((0,0,0))
visit[0][0]=1
ch=0
while q:
    x,y,life=q.popleft()
    if x==500 and y==500:
        res=life
        ch=1
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<=500 and 0<=ny<=500 and not visit[nx][ny]:
            if li[nx][ny]==0:
                q.appendleft((nx,ny,life))
                visit[nx][ny]=1
            elif li[nx][ny]==1:
                q.append((nx,ny,life+1))
                visit[nx][ny]=1
print(res if ch!=0 else -1)