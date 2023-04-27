from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
K=int(input().strip())

def dfs(graph,node,visit,co):
    global res
    visit[node]=1
    colors[node]=co
    for i in graph[node]:
        if not visit[i]:       
            dfs(graph,i,visit,-co)
        elif colors[i]==colors[node]:
            res="NO"
            return

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
    visit=[0]*(V+1)
    for i in range(1,V+1):
        if not visit[i]:
            dfs(graph,i,visit,1)
        if res=="NO":
            break
    print(res)