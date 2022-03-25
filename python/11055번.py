n=int(input())
a=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=0
dp[1]=a[1]
for i in range(2,n+1):
    for j in range(i):
        if a[i]>a[j]: # 자기자신보다 값이 작을때,
            dp[i]=max(dp[i],dp[j]+a[i]) # i번째까지의 총합과, j번재에서 i숫자를 더했을때 더 큰걸로
        else:
            dp[i]=max(dp[i],a[i]) # i번째숫자가 더 작을때는 i번째숫자를 추가못하므로, i번째와 i번째에서 최대값을 비교
print(max(dp))
    
    
# n번째에서 0~n-1번째까지, 자기자신보다 작고 그중 가장 큰 값의 길이를 구해 1을 더함
