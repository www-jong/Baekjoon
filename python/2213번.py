import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
li=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit=[0]*(N+1)
dp=[[[0,[]],[0,[]]] for _ in range(N+1)]
def func(x):
    visit[x]=1
    dp[x][1][1].append(x)
    dp[x][1][0]=li[x]
    for i in graph[x]:
        if not visit[i]:
            func(i)
            if dp[i][1][0]>dp[i][0][0]:
                dp[x][0][0]+=dp[i][1][0]
                dp[x][0][1]+=dp[i][1][1]
            else:
                dp[x][0][0]+=dp[i][0][0]
                dp[x][0][1]+=dp[i][0][1]
            dp[x][1][0]+=dp[i][0][0]
            dp[x][1][1]+=dp[i][0][1]


func(1)
if dp[1][0][0]>dp[1][1][0]:
    print(dp[1][0][0])
    print(*sorted(dp[1][0][1]))
else:
    print(dp[1][1][0])
    print(*sorted(dp[1][1][1]))