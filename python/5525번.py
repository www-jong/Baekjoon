N=int(input())
se=int(input())
S=input()
n_s='I'+'OI'*N
dp=[0]*(len(S))
for i in range(N,len(S)):
    if S[i-N:i]==N:
        dp[i]=dp[i-1]+1
print(dp[se-1])
