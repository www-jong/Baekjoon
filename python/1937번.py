import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

d=[0,0,1,-1]
dp = [[-1] * n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + d[i]
        ny = y + d[3-i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[nx][ny] > array[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]
res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))
print(res)