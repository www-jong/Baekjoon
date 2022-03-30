import sys
count=0
def dfs(graph,node):
    global count
    count=max(len(check),count)
    for i in range(4):
        sx=node[0]+dx[i]
        sy=node[1]+dy[i]
        if 1<=sx<=r and 1<=sy<=c:
            if graph[sx][sy] not in check:
                check.add(graph[sx][sy])
                dfs(graph,[sx,sy])
                check.remove(graph[sx][sy])
r,c=map(int,sys.stdin.readline().split())
graph=[['0']*(c+1)]
for i in range(r):
    graph.append(['0']+list(sys.stdin.readline()))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
check=set()
check.add(graph[1][1])
dfs(graph,[1,1])
print(count)

