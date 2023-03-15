N,M=map(int,input().split())
li=[[0]*(M+1)]
cctv=[]
cctv_stable=[]
end_res=N*M
dx=[0,1,0,-1]
dy=[1,0,-1,0]
cctv_ran=[0,[[0],[1],[2],[3]],
          [[0,2],[1,3],[0,2],[1,3]],
          [[0,1],[1,2],[2,3],[3,0]],
          [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]]


def look(x,y,dir,res,maps):
    for i in dir: # 1,2,3,4=왼, 아래, 오른, 위
        idx=1
        while True:
            nx=x+dx[i]*idx
            ny=y+dy[i]*idx
            if 1<=nx<=N and 1<=ny<=M and maps[nx][ny]!=6:
                if maps[nx][ny] not in {-1,1,2,3,4,5}:
                    res-=1
                    maps[nx][ny]=-1
            else:break
            idx+=1
    return res,maps

def func(cctv_info,maps,res,idx):
    global end_res
    if cctv_info!=0:
        res,maps=look(cctv_info[0],cctv_info[1],cctv_ran[cctv_info[2]][cctv_info[3]],res,maps)
    if idx>=len(cctv):
        end_res=min(end_res,res)
        return
    
    x,y,c=cctv[idx]
    for j in range(4):
        temp_maps=[row[:] for row in maps]
        temp_res=res
        func((x,y,c,j),temp_maps,temp_res,idx+1)


for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(M):
        if tmp[j]!=0:
            end_res-=1
            if tmp[j] in {1,2,3,4}:
                cctv.append([i+1,j+1,tmp[j]])
            if tmp[j]==5:
                cctv_stable.append([i+1,j+1,tmp[j]])
    li.append([0]+tmp)

for (x,y,_) in cctv_stable:
    for i in range(4):
        idx=1
        while True:
            nx=x+dx[i]*idx
            ny=y+dy[i]*idx
            if 1<=nx<=N and 1<=ny<=M and li[nx][ny]!=6:
                if li[nx][ny] not in {-1,1,2,3,4,5}:
                    end_res-=1
                    li[nx][ny]=-1
            else:break
            idx+=1

func(0,li,end_res,0)
print(end_res)
