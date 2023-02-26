from collections import deque
R,C=map(int,input().split())
st_x,st_y=0,0
end_x,end_y=0,0
dx,dy=[0,-1,0,1],[1,0,-1,0]
maps=[['X']*(C+1)]
times=[[0]*(C+1) for i in range(R+1)]
waters=[]

for i in range(1,R+1):
    S=['X']+list(input())
    for j in range(1,C+1):
        if S[j]=='S':
            st_x,st_y=i,j
            S[j]=500
        elif S[j]=='D':
            end_x,end_y=i,j
            S[j]=1000
        elif S[j]=='*':
            waters.append((i,j))
            S[j]=0
        elif S[j]=='X':
            S[j]=-1
        elif S[j]=='.':
            S[j]=500
    maps.append(S)

def water(x,y,time):
    global maps,tmp_waters
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 1<=nx<=R and 1<=ny<=C:
            if maps[nx][ny]==500:
                maps[nx][ny]=time
                tmp_waters.append((nx,ny))
            
for i in range(1,60):
    tmp_waters=[]
    for x,y in waters:
        water(x,y,i)
    waters+=tmp_waters.copy()

q=deque()
q.append((st_x,st_y))
while q:
    sx,sy=q.popleft()
    now_time=times[sx][sy]
    if (sx,sy)==(end_x,end_y):
        break
    for i in range(4):
        nx=sx+dx[i]
        ny=sy+dy[i]
        if 1<=nx<=R and 1<=ny<=C and maps[nx][ny]>1+now_time and times[nx][ny]==0:
            q.append((nx,ny))
            times[nx][ny]=now_time+1

if times[end_x][end_y]!=0:
    print(times[end_x][end_y])
else:
    print('KAKTUS')