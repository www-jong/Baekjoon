import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
N,M,R=map(int,input().split())

def dfs(graph,node,visit):
    global count
    visit[node]=count
    count+=1
    for i in graph[node]:
        if not visit[i]:
            dfs(graph,i,visit)
visit=[0]*(N+1)
graph=[[] for i in range(N+1)]
count=1
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort(reverse=True)
dfs(graph,R,visit)
for i in range(1,N+1):
    print(visit[i])