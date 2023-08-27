dx,dy=[1,-1,0,0],[0,0,1,-1]
def dfs(x,y,visit,li,move):
    global res
    if move==3:
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        plag=0
        while 0<=nx<N and 0<=ny<N:
            if li[nx][ny]==1 and not plag and not visit[nx][ny]:
                plag=1
            elif plag:
                if li[nx][ny] and not visit[nx][ny]:
                    res.add((nx,ny))
                    visit[nx][ny]=1
                    li[nx][ny]=0
                    dfs(nx,ny,visit,li,move+1)
                    visit[nx][ny]=0
                    li[nx][ny]=1
                    break
                elif not li[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny]=1
                    dfs(nx,ny,visit,li,move+1)
                    visit[nx][ny]=0
            nx+=dx[i]
            ny+=dy[i]

for m in range(int(input())):
    N=int(input())
    start=[]
    res=set()
    li=[]
    visit=[[0]*N for i in range(N)]
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in range(N):
            if tmp[j]==2:
                start=[i,j]
                tmp[j]=0
        li.append(tmp)
    g=dfs(start[0],start[1],visit,li,0)
    print(res)
    print(f'#{m+1}',len(res))