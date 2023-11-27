N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
r=N*M*2
d=[0,0,1,-1]
for x in range(N):
    for y in range(M):
        t=4*li[x][y]
        for k in range(4):
            nx,ny=x+d[k],y+d[3-k]
            if 0<=nx<N and 0<=ny<M:
                t-=min(li[x][y],li[nx][ny])

        r+=t
print(r)