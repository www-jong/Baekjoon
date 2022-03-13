n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i] and dp[i]<dp[j]: # 자기자신보다는 작지만, 자기때보단 길이가 길어야함(계속 자기자신떄 길이가 바뀌므로)
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))
    
    
# n번째에서 0~n-1번째까지, 자기자신보다 작고 그중 가장 큰 값의 길이를 구해 1을 더함
