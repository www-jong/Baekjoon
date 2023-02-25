N,M=map(int,input().split())
li=[]
dx,dy=[-1,0,1,0],[0,1,0,-1]  # 0,1,2,3 북동남서
visit=[[0]*(M) for i in range(N)]
r,c,d=map(int,input().split())
visit[r][c]=1
res=1
for i in range(N):
    li.append(list(map(int,input().split())))
while True:
    ch=0
    for i in range(1,5):
        nd=(d+3*i)%4
        nx=r+dx[nd]
        ny=c+dy[nd]
        if visit[nx][ny]==0 and li[nx][ny]==0:
            print(f'now : ({nx},{ny},{nd})')
            visit[nx][ny]=1
            r,c,d,ch=nx,ny,nd,1
            res+=1
            break
    if ch==0:
        nx=r+dx[d-2]
        ny=c+dy[d-2]
        if li[nx][ny]==0:
            print(f' back! ({nx},{ny},{d})')
            r,c=nx,ny
        else:
            break
print(res)
