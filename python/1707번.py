from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
K=int(input().strip())

def dfs(graph,node,visit):
    global res
    visit[node]=1
    for i in graph[node]:
        if not visit[i]:
            if colors[i]==colors[node]:
                res='NO'
                break
            dfs(graph,i,visit)

for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for i in range(V+1)]
    res='YES'
    for i in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    colors=[-1]*(V+1)
    check=[]
    for i in range(1,V+1):
        if colors[i]==-1:
            check.append(i)
            q=deque()
            q.append(i)
            colors[i]=1
            while q:
                x=q.popleft()
                nowcolor=colors[x]
                for j in graph[x]:
                    if colors[j]!=-1 and colors[j]==nowcolor:
                        res='NO'
                        break
                    if colors[j]==-1:
                        q.append(j)
                        colors[j]=0 if nowcolor else 1
    
    for i in check:
        visit=[0]*(V+1)
        dfs(graph,i,visit)
    print(res)