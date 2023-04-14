# dp실패
li=[0]+list(map(int,input().split()))
INF=10**9
dp=[[[INF]*(5) for i in range(5)] for _ in range(len(li)+1)]
dp[0][0][0]=0
def check(x,y):
    if x==y:
        return 1
    elif x==0 or y==0:
        return 2
    elif abs(x-y)%2==0:
        return 4
    else:
        return 3
for i in range(1,len(li)):
    now=li[i]
    for le in range(5):
        for ri in range(5):
            dp[i][now][ri]=min(dp[i][now][ri],dp[i-1][le][ri]+check(le,now))
            dp[i][le][now]=min(dp[i][le][now],dp[i-1][le][ri]+check(ri,now))
res=INF
for i in range(5):
    for j in range(5):
        res=min(res,dp[len(li)-2][i][j])
print(res)
'''
  1
2 0 4
  3
중앙 -> 사이드 : 2
사이드 -> 인접 : 3
사이드 -> 반대 : 4
같은지점 -> 1

dp[i][0]= [i번째에서 왼발일때 최소값,[왼,오]]
dp[i][1]= [i번째에서 오른발일때 최소값,[왼,오]]
l_dp[i][0]=[i번째에서 왼발일때 ]

'''