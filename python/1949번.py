import sys
sys.setrecursionlimit(10**9)
N=int(input())
li=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
res=0
dp=[[0,0] for _ in range(N+1)]
def func(visit,x):
    global dp
    visit[x]=1
    dp[x][1]=li[x]
    for i in graph[x]:
        if not visit[i]:
            func(visit,i)
            dp[x][0]+=max(dp[i])
            dp[x][1]+=dp[i][0]
func([0]*(N+1),1)
print(dp)
print(max(dp[1]))