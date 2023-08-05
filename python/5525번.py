N=int(input())
N='I'+'OI'*N
M=int(input())
S='d'+input()
res=0
dp=[0]*(M+1)
check=S[len(N)-1]
for i in range(len(N),M+1):
    if S[i]=='I' and S[i]!=check:
        dp[i]=dp[i-1]+(1 if S[i-len(N)+1:i+1]==N else 0)
        check=S[i]
    else:
        check=S[i]
        dp[i]=dp[i-1]
print(dp[M])