n=int(input())
def func1(n):
    if n==1 or n==2:
        return 1
    else:
        return (func1(n-1)+func1(n-2))
def func2(n):
    dp=[1]*(n+1)
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
for n in range(3,21):
    print("%d %d %d"%(n,func2(n),n-2))
