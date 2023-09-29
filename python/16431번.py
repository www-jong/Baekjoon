from collections import deque
bx,by=map(int,input().split())
dx,dy=map(int,input().split())
jx,jy=map(int,input().split())
J=abs(dx-jx)+abs(dy-jy)
q=deque()
q.append((bx,by,0))
visit=[[0]*(1001) for i in range(1001)]
visit[bx][by]=1
d=[[1,1],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1],[0,1],[0,-1]]
while q:
    x,y,c=q.popleft()
    for i in range(8):
        nx=x+d[i][0]
        ny=y+d[i][1]
        if 0<=nx<=1000 and 0<=ny<=1000 and not visit[nx][ny]:
            q.append((nx,ny,c+1))
            visit[nx][ny]=c+1
if visit[jx][jy]<J:
    print('bessie')
elif visit[jx][jy]>J:
    print('daisy')
else:
    print('tie')