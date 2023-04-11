A=input()
B=input()
dp=[[[0,'']]*(len(B)+1) for i in range(len(A)+1)]
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=[dp[i-1][j-1][0]+1,dp[i-1][j-1][1]+A[i-1]]
        else:
            if dp[i-1][j][0]>=dp[i][j-1][0]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
if dp[-1][-1][0]==0:
    print(0)
else:
    print(dp[-1][-1][0])
    print(dp[-1][-1][1])

"""
dp=[A의길이][B의길이]
dp[i][j]= A의 i번째와 B의 j번째에서 최장공통부분수열의 값
즉, A[i]와 B[i]가 같을경우, dp[i-1][j-1]에서 1을 더한값
 다를경우, dp[i][j-1]과 dp[i-1][j]중 큰값.
"""