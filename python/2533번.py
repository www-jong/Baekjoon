import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

N=int(input())
tree=[[] for i in range(N+1)]
res=[0,0]
for i in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
visit=[0]*(N+1)
dp=[[0,0] for i in range(N+1)]
def dfs(st):
    global tree
    global visit
    visit[st]=1
    if not len(tree[st]):
        dp[st][1]=1
        dp[st][0]=0
    else:
        for i in tree[st]:
            if not visit[i]:
                dfs(i)
                dp[st][1]+=min(dp[i][0],dp[i][1])
                dp[st][0]+=dp[i][1]
        dp[st][1]+=1
dfs(1)
print(min(dp[1][0],dp[1][1]))