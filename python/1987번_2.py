import sys
count=1
def bfs(x,y):
    q=set()
    q.add((x,y,graph[x][y]))
    global count
    while q:
        x,y,ans=q.pop()
        for i in range(4):
            sx=x+dx[i]
            sy=y+dy[i]
            if 1<=sx<=r and 1<=sy<=c and graph[sx][sy] not in ans:
                q.add((sx,sy,ans+graph[sx][sy]))
                count=max(len(ans)+1,count)
r,c=map(int,sys.stdin.readline().split())
graph=[['0']*(c+1)]
for i in range(r):
    graph.append(['0']+list(sys.stdin.readline()))
visits=[[0]*(c+1) for i in range(r+1)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
bfs(1,1)
print(count)

