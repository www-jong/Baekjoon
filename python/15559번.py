import sys
input=sys.stdin.readline
def dfs(x,y,c):
    global r,visit
    visit[x][y]=c
    nx,ny=x+d[li[x][y]][0],y+d[li[x][y]][1]
    if not visit[nx][ny]:
        dfs(nx,ny,c)
    else:
        if visit[nx][ny]==c:
            r+=1


N,M=map(int,input().split())
li=[input().rstrip() for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
d={'N':[-1,0],'S':[1,0],'W':[0,-1],'E':[0,1]}
r=0
c=1
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            dfs(i,j,c)
            c+=1
            print(i,j)
            #r+=1
print(r)