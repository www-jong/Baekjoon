n,k=map(int,input().split())
arr=[]
count=0
dp=[[0]*(k+1) for i in range(n+1)]
for i in range(1,n+1):
    dp[i][1]=1
for i in range(1,k+1):
    dp[1][i]=i
for i in range(2,n+1):
    for j in range(2,k+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[n][k]%1000000000)
print(dp)
'''
dp[i][k]= 정수k개를 더해 i가 되는 경우의수
dp[i][x]=dp[i][x-1]에서0을 더한방법+dp[i-1][x]에서...
아오

k=  1  2  3  4  5
0   1  1  1  1  1
1   1  2  3  4  5
2   1  3  6  10 15
3   1  4  10 15 21
4   1  5  15 30 51
5   1  6  21 51 102
위 표를 식으로 나타내면 dp[i][j]=dp[i-1][j]+dp[i][j-1]이 됨

다른 아이디어로는
dp[n][k]는 dp[0][k-1]+dp[1][k-1]...dp[n][k-1]를 합친것.
'''