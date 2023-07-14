from collections import deque
N,M=map(int,input().split())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

li=[[0]]
for i in range(N):
    li.append([0]+list(map(int,input().split())))

#1, 섬 체크
islands=[]
islands_idx=-1
already_islands={}
visit=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if li[i][j]==0 or str(i)+'_'+str(j) in already_islands:
            continue
        already_islands[str(i)+'_'+str(j)]=1
        islands_idx+=1
        islands.append([(i,j)])
        q=deque()
        q.append((i,j))
        visit[i][j]=1
        while q:
            x,y=q.popleft()
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if 1<=nx<=N and 1<=ny<=M:
                    if visit[nx][ny]==0 and li[nx][ny]==1:
                        islands[islands_idx].append((nx,ny))
                        already_islands[str(nx)+'_'+str(ny)]=1
                        q.append((nx,ny))
                        visit[nx][ny]=1

#섬간 모든 라인 구하기
corse=[]
nodes=[i for i in range(len(islands)+1)]

def get_line(s1,s2):
    tmps=0
    if s1[0]!=s2[0] and s1[1]!=s2[1]:
        return -1
    elif s1[1]==s2[1] and abs(s2[0]-s1[0])>=3:
        for o in range(min(s1[0],s2[0])+1,max(s1[0],s2[0])):
            if str(o)+'_'+str(s1[1]) not in already_islands:
                tmps+=1
            else:
                return -1
    elif s1[0]==s2[0] and abs(s2[1]-s1[1])>=3:
        for o in range(min(s1[1],s2[1])+1,max(s1[1],s2[1])):
            if str(s1[0])+'_'+str(o) not in already_islands:
                tmps+=1
            else:
                return -1
    else:
        return -1
    return tmps

for i in range(len(islands)):
    for j in range(i+1,len(islands)):
        for s1 in islands[i]:
            for s2 in islands[j]:
                val=get_line(s1,s2)
                if val!=-1:
                    corse.append([i,j,val])
                    corse.append([j,i,val])

#유니온파인드
def find(a):
    if nodes[a]==a:
        return a
    else:
        nodes[a]=find(nodes[a])
        return nodes[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b

if len(corse)!=0 and len(islands)<=(len(corse)//2)+1:
    corse.sort(key=lambda x:x[2])
    i=0
    cnt=0
    weight=0
    while cnt<len(islands)-1:
        try:
            a,b,c=corse[i]
            if find(a)!=find(b):
                cnt+=1
                weight+=c
                union(a,b)
            i+=1
        except IndexError:
            weight=-1
            break
    print(weight)
else:
    print(-1)