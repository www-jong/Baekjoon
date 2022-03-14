n=int(input())
s=[[0,0]]
for i in range(n):
    s.append(list(map(int,input().split())))
dp=[[0]*6 for i in range(n+1)]
dp[1][s[1][0]]=s[1][1]

for i in range(2,n+1):
    if (n-i+1)>=s[i][0]:
        dp[i][s[i][0]]=max(dp[i-1][1]+s[i][1],dp[i-1][0]+s[i][1])
    dp[i][0]=max(dp[i-1][1],dp[i-1][0])
    for j in range(1,5):
        dp[i][j]=max(dp[i-1][j+1],dp[i][j])
print(max(dp[n][0],dp[n][1]))

"""
dp[i][j]=x : i일째, 상담일수가 j일 남았을때 최대금액x
1. i일째 상담을 할 때
 1-1 : i-1일째 남은일수가 1일일때
 1-2 : i-1일째 남은일수가 0일일때
dp[i][s[i][0]]=max(dp[i-1][1]+s[i][1],dp[i-1][0]+s[i][1])
2. i일째 상담이 가능한데 안할때
 2-1 : i-1일째 남은일수가 1일일때
 2-2 : i-1일째 남은일수가 0일일때
3. i일째 상담이 불가능할때
 dp[i][j]=max(dp[i-1][j+1],dp[i][j])

결과 : max(dp[n][0],dp[n][1]) 을 구해야 함(마지막날도 상담이 하루 가능하므로)
"""