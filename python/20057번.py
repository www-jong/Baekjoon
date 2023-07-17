N=int(input())
li=[[0]]
dx=[0,1,0,-1,0,1,0,-1]  # 왼쪽, 아래쪽,오른쪽,위쪽
dy=[-1,0,1,0,-1,0,1,0]
idx=[-1]
count=[0,1,0]
res=0
while count[2]<((1+N)**2):
    idx+=[count[0]]*count[1] 
    if count[0]==3:count[0]=0
    else:count[0]+=1
    idx+=[count[0]]*count[1]
    if count[0]==3:count[0]=0
    else:count[0]+=1
    
    count[2]+=count[1]*2
    count[1]+=1

def check(x,y):
    if 1<=x<=N and 1<=y<=N:
        return True
    return False

def blow(x,y,sand):
    global res
    if check(x,y):
        li[x][y]+=(sand//1)
    else:
        res+=(sand//1)
    return (sand//1)

def tornado(x,y,dirc):
    global li,res
    now_sand=li[x][y]
    blow_sand=0
    blow_sand+=blow(x+dx[dirc]*2,y+dy[dirc]*2,now_sand*0.05)
    blow_sand+=blow(x+dx[dirc]+dx[dirc-1],y+dy[dirc]+dy[dirc-1],now_sand*0.1)
    blow_sand+=blow(x+dx[dirc]+dx[dirc+1],y+dy[dirc]+dy[dirc+1],now_sand*0.1)
    blow_sand+=blow(x+dx[dirc+1],y+dy[dirc+1],now_sand*0.07)
    blow_sand+=blow(x+dx[dirc+1]*2,y+dy[dirc+1]*2,now_sand*0.02)
    blow_sand+=blow(x+dx[dirc-1],y+dy[dirc-1],now_sand*0.07)
    blow_sand+=blow(x+dx[dirc-1]*2,y+dy[dirc-1]*2,now_sand*0.02)
    blow_sand+=blow(x+dx[dirc+2]+dx[dirc+1],y+dy[dirc+2]+dy[dirc+1],now_sand*0.01)
    blow_sand+=blow(x+dx[dirc+2]+dx[dirc-1],y+dy[dirc+2]+dy[dirc-1],now_sand*0.01)
    if check(x+dx[dirc],y+dy[dirc]):
        li[x+dx[dirc]][y+dy[dirc]]+=now_sand-blow_sand
    else:
        res+=now_sand-blow_sand
    li[x][y]=0

for i in range(N):
    li.append([0]+list(map(int,input().split())))

now_x=N//2+1
now_y=N//2+1
for i in range(1,N**2+1):
    now_x+=dx[idx[i]]
    now_y+=dy[idx[i]]
    tornado(now_x,now_y,idx[i])

print(int(res))
