import sys
input=sys.stdin.readline

def f(x,y,a,b):
    return abs(x-a)+abs(y-b)
N=int(input())
W=int(input())
eve=[()]
for i in range(W):
    a,b=map(int,input().split())
    eve.append((a,b))
dp=[[[0,(0,0),(0,0),[]] for i in range(W+1)] for i in range(W+1)]
dp[1][0]=[f(*eve[1],1,1),eve[1],(N,N),[0,0,1]]
dp[0][1]=[f(*eve[1],N,N),(1,1),eve[1],[0,0,2]]
dp[0][0]=[0,(1,1),(N,N),[]]
for i in range(1,W+1):
    dp[0][i]=[dp[0][i-1][0]+f(*eve[i],*dp[0][i-1][2]),dp[0][i-1][1],eve[i],[0,i-1,2]]
    dp[i][0]=[dp[i-1][0][0]+f(*eve[i],*dp[i-1][0][1]),eve[i],dp[i-1][0][2],[i-1,0,1]]
for i in range(W+1):
    tmp_mins=[(10**8,(),(),[]),(10**8,(),(),[])]
    if i!=W and i!=0:
        for j in range(i):
            #print(f'{i}:{j} -> {i+1} , {(dp[i][j][0]+f(*eve[i+1],*dp[i][j][2]))} {tmp_mins[0][0]}')
            if  tmp_mins[0][0]>(dp[i][j][0]+f(*eve[i+1],*dp[i][j][2])):
                tmp_mins[0]=[(dp[i][j][0]+f(*eve[i+1],*dp[i][j][2])),dp[i][j][1],eve[i+1],[i,j,2]]
            if  tmp_mins[1][0]>(dp[j][i][0]+f(*eve[i+1],*dp[j][i][1])):
                tmp_mins[1]=[(dp[j][i][0]+f(*eve[i+1],*dp[j][i][1])),eve[i+1],dp[j][i][2],[j,i,1]]
        dp[i][i+1]=tmp_mins[0]
        dp[i+1][i]=tmp_mins[1]
    for j in range(i+2,W+1):

        dp[i][j]=[dp[i][j-1][0]+f(*eve[j],*dp[i][j-1][2]),dp[i][j-1][1],eve[j],[i,j-1,2]]
        dp[j][i]=[dp[j-1][i][0]+f(*eve[j],*dp[j-1][i][1]),eve[j],dp[j-1][i][2],[j-1,i,1]]

res=[10**9,[]]
for i in range(W):
    if res[0]>dp[i][W][0]:
        res=[dp[i][W][0],dp[i][W][3]]
    if res[0]>dp[W][i][0]:
        res=[dp[W][i][0],dp[W][i][3]]

print(res[0])
r=[]
now=res[1]
for i in range(W):
    r=[now[2]]+r
    now=dp[now[0]][now[1]][3]
for i in r:
    print(i)

for i in dp:
    for j in i:
        print(j[0],end=" ")
    print()
