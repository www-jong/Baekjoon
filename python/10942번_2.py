import sys
n=int(sys.stdin.readline())
arr=[0]+list(map(int,sys.stdin.readline().split()))
m=int(input())
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=1
for i in range(1,n):
    if arr[i]==arr[i+1]:
        dp[i][i+1]=1
for i in range(1,n-1):
    for j in range(2,n-i+1):
        if dp[i+1][i+j-1]==1 and arr[i]==arr[i+j]:
            dp[i][i+j]=1
for i in range(m):
    q,w=map(int,sys.stdin.readline().split())
    print(dp[q][w])
