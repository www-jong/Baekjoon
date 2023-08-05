from collections import deque
N,M=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
li=[]
start=[0,0]
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]=='I':
            start=[i,j]
            tmp=tmp[:j]+'O'+tmp[j+1:]
    li.append(tmp)
res=0
visit=[[0]*(M) for i in range(N)]
q=deque()
q.append(start)
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and li[nx][ny]!='X':
            if visit[nx][ny]==0:
                visit[nx][ny]=1
                q.append((nx,ny))
                if li[nx][ny]=='P':
                    res+=1
print(li)
print(res if res !=0 else 'TT')