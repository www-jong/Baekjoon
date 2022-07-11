import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dp=[0]*(n+1)
count=0
li=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    dp[i]=dp[i-1]+li[i]
max=dp[n]
for i in range(1,n+1):
    if dp[i]%m==0:
        count+=1
    if (max-dp[i-1])%m==0:
        count+=1
    
print(count)
print(dp)