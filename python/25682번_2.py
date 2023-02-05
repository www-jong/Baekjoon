# 시간초과!
import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
li=[[0]*(M+1)]
res=0
def check(color):
    dp=[[0]*(M+1) for i in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,M+1):
            if (i+j)%2==0:
                val=li[i][j]!=color
            else:
                val=li[j][j]==color
            dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]-dp[i][j]+val
    tmp=10**9
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            tmp=min(tmp,dp[i+K-1][j+K-1]-dp[i+K-1][j-1]-dp[i-1][j+K-1]+dp[i-1][j-1])
    return tmp
for i in range(N):
    li.append([0]+list(input()))

print(check('W'))
print(check('B'))

'''
세로 N
가로 M

'''