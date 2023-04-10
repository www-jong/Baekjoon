from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

mx,my=map(int,input().split())
count=[0,0]
cheeses=[]
li=[[0]*(my+1)]
for i in range(mx):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,my+1):
        if tmp[j]==1:
            cheeses.append([i,j])
    li.append(tmp)
    count[1]+=sum(tmp)

q=deque()
q.append((1,1))
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=mx and 1<=ny<=my:
            if li[nx][ny]==0:
                q.append((nx,ny))
                li[nx][ny]=2
tmp_c=0
while tmp_c<count[1]:
    q=deque()
    q.append((1,1))
    visit=[[0]*(my+1) for i in range(mx+1)]
    visit[1][1]=1
    tmp_airs={}
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=mx and 1<=ny<=my:
                if li[nx][ny]==0:
                    q.append((nx,ny))
                    li[nx][ny]=2
                    visit[nx][ny]=1
                elif li[nx][ny]==1:
                    if (nx,ny) in tmp_airs:
                        tmp_airs[(nx,ny)]+=1
                    else:
                        tmp_airs[(nx,ny)]=1
                elif li[nx][ny]==2 and visit[nx][ny]==0:
                    q.append((nx,ny))
                    visit[nx][ny]=1

    for k,v in tmp_airs.items():
        if v>=2:
            li[k[0]][k[1]]=2
            tmp_c+=1
    count[0]+=1    

print(count[0])
