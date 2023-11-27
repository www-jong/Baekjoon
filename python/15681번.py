import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N,R,Q=map(int,input().split())
graph=[[] for _ in range(N+1)]
visit=[0]*(N+1)
for i in range(N-1):
    U,V=map(int,input().split())
    graph[U].append(V)
    graph[V].append(U)
def dfs(x):
    visit[x]=1
    for i in graph[x]:
        if not visit[i]:
            dfs(i)
            visit[x]+=visit[i]
dfs(R)
for i in range(Q):
    print(visit[int(input())])