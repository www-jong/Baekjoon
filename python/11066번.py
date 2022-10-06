import sys
input=sys.stdin.readline()
for _ in range(int(input())):
    K=int(input())
    li=[0]+list(map(int,input().split()))
    dp=[[0]*(K+1) for _ in range(K+1)]
    # dp[i][j] = i부터 j까지 합치는데 최소비용
    S=[0 for _ in range(K+1)]
    for i in range(1,K+1):
        S[i]=S[i-1]+li[i]
        
    for i in range(2,K+1):
        for j in range(1,K+2-i):
