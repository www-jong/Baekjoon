for _ in range(int(input())):
    n=int(input())
    lis=[]
    for _ in range(2):
        lis.append([0]+list(map(int,input().split())))
    dp=[[0,0,0] for i in range(n+1)]
    dp[1][0]=0
    dp[1][1]=lis[0][1]
    dp[1][2]=lis[1][1]
   
    for i in range(2,n+1):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+lis[0][i]
        dp[i][2]=max(dp[i-1][0],dp[i-1][1])+lis[1][i]
    print(max(dp[n]))
        
"""
list=[[1,23,5,15,113,3],[1,124,21,523,5325,..]]
즉, [2개][n개] 리스트다
dp[i][0]= i번째 스티커열에서 스티커를 안고를때의 최대값
dp[i][1]= i번째스티커열에서 1번째스티커를 고를때의 최대값
dp[i][2]= i번째 스티커열에서 2번째 스티커를 고를떄의 최대값

"""