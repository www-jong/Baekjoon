from collections import deque
n,m=map(int,input().split())
graph=[[0]*(m+1)]
visit=[[0]*(m+1) for i in range(n+1)]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))
well=[]
we=[]
def wellmake(we):
    global well
    if len(we)==3:
        well.append(we[:])
        return
    for a in range(1,n+1):
        for b in range(1,m+1):
            if graph[a][b]==2 or graph[a][b]==1:
                continue
            if [a,b] in we:
                continue
            we.append([a,b])
            wellmake(we)
            we.pop()
wellmake(we)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
count_list=0
for wes in well:
    for i in range(3):
        graph[wes[i][0]][wes[i][1]]=1
    visit=[[0]*(m+1) for i in range(n+1)]
    count=0
    for aa in range(1,n+1):
        for bb in range(1,m+1):
            if graph[aa][bb]==0 and visit[aa][bb]==0:
                q=deque()
                q.append((aa,bb))
                visit[aa][bb]=1
                check=1
            else:continue
            while q:
                x,y=q.popleft()
                for i in range(4):
                    sx=x+dx[i]
                    sy=y+dy[i]
                    if 0<sx<=n and 0<sy<=m:
                        if graph[sx][sy]==2:
                            check=0
                            break
                        elif graph[sx][sy]==0 and visit[sx][sy]==0:
                            q.append((sx,sy))
                            visit[sx][sy]=1
                            check+=1
            count+=check                          
    for i in range(3):
        graph[wes[i][0]][wes[i][1]]=0
    if count>count_list:
        count_list=count
print(count_list)
"""
빈공간에서 바이러스가 있을시, 카운트하지않는방법
너무느리다
"""