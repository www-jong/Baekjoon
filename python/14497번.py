from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
N,M=map(int,input().split())
x1,y1,x2,y2=map(lambda x:int(x)-1,input().split())
li=[input().rstrip() for i in range(N)]
visit=[[-1]*(M)for i in range(N)]
li[x1]=li[x1][:y1]+'1'+li[x1][y1+1:]
li[x2]=li[x2][:y2]+'1'+li[x2][y2+1:]


q=deque()
q.append((x1,y1,0))
visit[x1][y1]=0
while q:
    x,y,c=q.popleft()
    if x==x2 and y==y2:
        print(c)
        break
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<N and 0<=ny<M:
            if visit[nx][ny]==-1:
                if li[nx][ny]=='0':
                    visit[nx][ny]=c
                    q.appendleft((nx,ny,c))
                else:
                    visit[nx][ny]=c+1
                    q.append((nx,ny,c+1))