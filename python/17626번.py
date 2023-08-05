n=int(input())

dp=[4]*(50001)
dic,li={},[]
for i in range(1,226):
    if i*i<=50000:
        dp[i*i]=1
    dic[i*i]=1
    li.append(i*i)
idx=0
for i in range(2,n+1):
    while li[idx]<=i:
        idx+=1
    idx-=1
    dp[i]=min(dp[i-1]+1,dp[i],dp[li[idx]]+dp[i-li[idx]])
    for j in range(1,idx):
        dp[i]=min(dp[li[j]]+dp[i-li[j]],dp[i])
print(dp[1:100])
print(dp[n])