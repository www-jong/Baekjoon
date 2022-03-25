n,k=map(int,input().split())
dp=[0]*(k+1)
coin=[]
for i in range(n):
    coin.append(int(input()))
dp[0]=1    

for i in coin:
    for j in range(1,k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
print(dp[k])

"""
dp[i]= dp[i-coin]을 더한 것. 
중복은 dp[i-coin]에서 처리가 다 됬기 때문에,(직접 중복은 처리하지않았지만 논리적으로 처리됨)
근데 ,coin은 가장 낮은것부터 반복    
"""