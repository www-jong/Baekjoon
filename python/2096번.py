import sys
input=sys.stdin.readline
N=int(input())
li=[]
max_dp=[[0,0,0],[0,0,0]]
min_dp=[[0,0,0],[0,0,0]]
tmp=list(map(int,input().split()))
max_dp[0],max_dp[1]=tmp[:],tmp[:]
min_dp[0],min_dp[1]=tmp[:],tmp[:]
for i in range(1,N):
    tmp=list(map(int,input().split()))
    max_dp[1][0]=max(max_dp[0][0],max_dp[0][1])+tmp[0]
    max_dp[1][1]=max(max_dp[0])+tmp[1]
    max_dp[1][2]=max(max_dp[0][1],max_dp[0][2])+tmp[2]
    min_dp[1][0]=min(min_dp[0][0],min_dp[0][1])+tmp[0]
    min_dp[1][1]=min(min_dp[0])+tmp[1]
    min_dp[1][2]=min(min_dp[0][1],min_dp[0][2])+tmp[2]
    max_dp.pop(0)
    min_dp.pop(0)
    max_dp.append([0,0,0])
    min_dp.append([0,0,0])

print(max(max_dp[0]),min(min_dp[0]))