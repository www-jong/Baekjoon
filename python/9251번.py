A=['a']+list(input())
B=['a']+list(input())
dp=[[0]*len(B) for i in range(len(A))]
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[len(A)-1][len(B)-1])


"""
dp=[A의길이][B의길이]
dp[i][j]= A의 i번째와 B의 j번째에서 최장공통부분수열의 값
즉, A[i]와 B[i]가 같을경우, dp[i-1][j-1]에서 1을 더한값
 다를경우, dp[i][j-1]과 dp[i-1][j]중 큰값.
"""