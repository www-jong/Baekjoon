import sys
input=sys.stdin.readline
T=int(input())
res=[]
for _ in range(T):
    K=int(input())
    li=list(map(int,input().split()))
    dp=[[0]*K for _ in range(K)]
    sums=[0]*K
    for i in range(K-1):
        dp[i][i+1]=li[i]+li[i+1]
        sums[i]=sums[i-1]+li[i] if i!=0 else li[0]
    sums[K-1]=sums[K-2]+li[K-1]
    for i in range(K):
        for j in range(i+2,K):
            
            min_v=10**9
            for k in range(i+1,j):
                min_v=min(min_v,dp[i][k]+dp[k][j])
            dp[i][j]=min_v+sums[j]-sums[i-1]
    res.append(dp[0][K-1])
print(res)


'''
i,j,k=0,1,
dp[i][j]=i부터 j까지의 최소 합 비용
-> (dp[i][k]+dp[k][j]) i<k<j에서 최소값+ i에서 j까지의 숫자합
dp[i][j]=min(dp[i][k]+dp[k][j]), k=i+1 to j-1
'''