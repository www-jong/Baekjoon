from collections import deque
N,M=map(int,input().split())
li=[[0]]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
vi=[]
all_selected_vi=[]
count=0
for i in range(1,N+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,N+1):
        if tmp[j]==2:
            vi.append([i,j])
        if tmp[j]==0:
            count+=1
    li.append(tmp)
len_vi=len(vi)

def choices(M,selected_vi,idx):
    global all_selected_vi
    if len(selected_vi)==M:
        all_selected_vi.append(selected_vi.copy())
        return
    
    for i in range(idx,len_vi):
        selected_vi.append(vi[i])
        choices(M,selected_vi,i+1)
        selected_vi.pop()

choices(M,[],0)
res=10**9
tmp_vi=[]
for choice_vi in all_selected_vi:
    li2=li.copy()
    visit=[[0]*(N+1) for i in range(N+1)]
    tmp_vi=choice_vi.copy()
    co=[0,0]
    print(f'now virus : {tmp_vi}')
    while tmp_vi and (co[1]!=count):
        q=deque()
        for x,y in tmp_vi:
            q.append((x,y))
            visit[x][y]=1
        tmp_vi=[]
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 1<=nx<=N and 1<=ny<=N:
                    if (li2[nx][ny]==0 or li2[nx][ny]==2) and visit[nx][ny]==0:
                        tmp_vi.append((nx,ny))
                        visit[nx][ny]=1
                        co[1]+=(1 if li2[nx][ny]==0 else 0)
                        print(f'co : {co}, {nx}:{ny} ...{3 if li2[nx][ny]==0 else -3}')
                        #li2[nx][ny]=2
        co[0]+=1

    print(f'res! : {co[0]},{res}')
    if co[1]!=0 and co[1]==count:
        res=min(co[0],res)
    elif co[1]==0 and co[1]==count:
        res=min(co[0],res)
for i in li:
    print(li)    
print(-1 if res==10**9 else res)