n=int(input())
li=list(map(int,input().split()))
dp=[1]*n
dp2=[1]*n

for i in range(n-1):
    if li[i+1]>=li[i]:
        dp[i+1]+=dp[i]
for i in range(n-1):
    if li[i+1]<=li[i]:
        dp2[i+1]+=dp2[i]
print(max(max(dp),max(dp2)))