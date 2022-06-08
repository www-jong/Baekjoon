import sys
from collections import deque
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
maps=[[0]*(N+1) for i in range(N+1)]
for i in range(K):
    x,y=map(int,input().split())
    maps[x][y]=2
L=int(sys.stdin.readline())
count=0
q=deque()
move=deque()
movelist=[(0,1),(1,0),(0,-1),(-1,0)] # 우 하 좌 상
movenum=0
check=0
q.append((1,1))
for i in range(L):
    x,c=map(str,sys.stdin.readline().split())
    x=int(x)
    move.append((x,c))
maps[1][1]=1
while True:
    if move:
        x,c=move.popleft()
    else:
        x=10001
    while True:
        if count==x:
            if c=='L':
                movenum=3 if movenum==0 else movenum-1
            else:
                movenum=0 if movenum==3 else movenum+1
            break
        sx,sy=q[-1]
        sx2=sx+movelist[movenum][0]
        sy2=sy+movelist[movenum][1]
        count+=1
        if 1<=sx2<=N and 1<=sy2<=N and (sx2,sy2) not in q:
            q.append((sx2,sy2))
            if maps[sx2][sy2]!=2:
                gx,gy=q.popleft()
                maps[sx2][sy2]=1
            else:
                maps[sx2][sy2]=1
        else:
            check=1
            break
    if check==1:
        break
print(count)
    
