import sys
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline

N=int(input())
nodes=[0]*(N+1)
depth=[0]*(N+1)
cal=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,dep):
    cal[x]=1
    depth[x]=dep
    for y in graph[x]:
        if cal[y]:
            continue
        nodes[y]=x
        dfs(y,dep+1)

def lca(a,b):
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=nodes[a]
        else:
            b=nodes[b]
    while a!=b:
        a=nodes[a]
        b=nodes[b]
    return a
dfs(1,0)
M=int(input())
for i in range(M):
    a,b,=map(int,input().split())
    print(lca(a,b))