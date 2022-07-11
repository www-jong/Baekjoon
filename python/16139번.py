import sys
input=sys.stdin.readline
s="P"+input().strip()
dp=[[0]*26 for i in range(len(s)+1)]
for i in range(1,len(s)):
    for j in range(26):
        dp[i][j]=dp[i-1][j]
    dp[i][ord(s[i])-97]+=1
n=int(input())
for i in range(n):
    a,b,c=map(str,input().strip().split())
    print(dp[int(c)+1][ord(a)-97]-dp[int(b)][ord(a)-97])
# pypy3 필수