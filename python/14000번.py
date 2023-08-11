n=int(input())
a=[0]+list(map(int,input().split()))
dp=[[0,[a[i]]] for i in range(n+1)]
dp[1]=[1,[a[1]]]
for i in range(2,n+1):
    for j in range(i):
        if a[j]<a[i] and dp[i][0]<dp[j][0]: 
            dp[i]=[dp[j][0],dp[j][1]+[a[i]]]
    dp[i][0]+=1
dp.sort(key=lambda x:x[0])
print(dp[-1][0])
print(*dp[-1][1])