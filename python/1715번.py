'''
dp를 이용한 방법 ->(11066번참고) 메모리초과
'''

N=int(input())
li=[0]
dp=[[0]*(N+1) for _ in range(N+1)]
sums=[0]*(N+1)
for i in range(N):
    li.append(int(input()))
for i in range(1,N+1):
    dp[i-1][i]=li[i-1]+li[i]
    sums[i]=sums[i-1]+li[i]
for k in range(2,N+1):
    for i in range(1,N+1):
        if i+k>N:
            break
        min_v=10**9
        for j in range(i,i+k):
            min_v=min(min_v,dp[i][j]+dp[j+1][i+k])
        dp[i][i+k]=min_v+sums[i+k]-sums[i-1]
print(dp[1][N])


'''
dp[i]=min(dp[i-1]+li[i],dp[i-2]+li[i-1]+li[i])
'''