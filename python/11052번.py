n=int(input())
s=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=s[i]
for i in range(2,n+1):
    for j in range(1,i):
        dp[i]=max(dp[i-j]+s[j],dp[i])
print(dp[n])

"""
s[i]=x : i개의 카드비용 x
dp[i]=x : i개의 카드를 가지고 있을때, 최대값 x 
dp[i]=max(dp[i-1]+s[i],dp[i-2]+s[2],...)
"""