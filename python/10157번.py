C,R=map(int,input().split())
li=[[0]*(R+1) for _ in range(C+1)]
dic={}
dx=[0,1,0,-1]
dy=[1,0,-1,0]
idx=0
x,y=1,1
li[1][1]=1
dic[1]=[1,1]
for i in range(2,(C*R)+1):
    nx=x+dx[idx]
    ny=y+dy[idx]
    if 1<=nx<=C and 1<=ny<=R and li[nx][ny]==0:
        li[nx][ny]=i
        dic[i]=[nx,ny]
    else:
        idx=(idx+1 if idx!=3 else 0)
        nx=x+dx[idx]
        ny=y+dy[idx]
        li[nx][ny]=i
        dic[i]=[nx,ny]
    x=nx
    y=ny
res=int(input())
if res>R*C:
    print(0)
else:
    print(*dic[res])