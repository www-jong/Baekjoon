N,M=map(int,input().split())
li=[[0]*(M+1)]
li_sum=[[0]*(M+1) for i in range(N+1)]
for i in range(N):
    li.append([0]+list(map(int,input().split())))
for i in range(1,N+1):
    for j in range(1,M+1):
        li_sum[i][j]=li_sum[i][j-1]+li_sum[i-1][j]+li[i][j]-li_sum[i-1][j-1]

K=int(input())
for i in range(K):
    i,j,x,y=map(int,input().split())
    val=li_sum[x][y]-li_sum[x][j-1]-li_sum[i-1][y]+li_sum[i-1][j-1]
    print(val)