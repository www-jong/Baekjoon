"""
조건 : n자리인데, 0으로시작하지않고, 1이 두번연속으로 나타나지 않아야함 

dp[i][1]= i자리인데, 1로시작하는 경우 --> dp[i-1][0] (dp[i-1][1]은 1이 연속으로 존재하지 않아야하는 조건에 의해 탈락)
dp[i][0]= i자리인데, 0으로 시작하는 경우 --> dp[i-1][0]+dp[i-1][1]
"""
n=int(input())
dp=[[1,1] for i in range(n+1)]
for i in range(2,n+1):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]
    dp[i][1]=dp[i-1][0]
print(dp[n][1])
    