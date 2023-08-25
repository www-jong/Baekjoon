N=int(input())
M=int(input())
INF=10**9
li=[[INF]*(N+1) for i in range(N+1)]
root=[[[]for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    li[i][i]=0
for i in range(M):
    a,b,c=map(int,input().split())
    li[a][b]=min(c,li[a][b])

for sta in range(1,N+1):
    for st in range(1,N+1):
        for end in range(1,N+1):
            if li[st][end]>li[st][sta]+li[sta][end]:
                li[st][end]=min(li[st][end],li[st][sta]+li[sta][end])
                root[st][end]=root[st][sta]+[sta]+root[sta][end]
for i in range(1,N+1):
    for j in range(1,N+1):
        if li[i][j]==INF:
            li[i][j]=0
for i in range(1,N+1):
    print(*li[i][1:])
for i in range(1,N+1):
    for j in range(1,N+1):
        if not li[i][j]:
            print(0)
        else:
            print(len(root[i][j])+2,i,*root[i][j],j)