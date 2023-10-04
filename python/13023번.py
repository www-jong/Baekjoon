import sys
input=sys.stdin.readline
def dfs(node,visit,d):
    global res
    print(visit,d)
    if res:
        return
    if d==5:
        res=1
        return
    for i in graph[node]:
        if not visit[i]:
            visit[i]=1
            dfs(i,visit,d+1)
            visit[i]=0

N,M=map(int,input().split())
graph=[[] for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

res=0
for i in range(N):
    if not res:
        v=[0]*N
        v[i]=1
        dfs(i,v,1)
print(res)