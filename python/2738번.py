N,M=map(int,input().split())
liN=[]
liM=[]
for i in range(N):
    liN.append(list(map(int,input().split())))
for i in range(N):
    liM.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        liN[i][j]+=liM[i][j]
for i in range(N):
    print(*liN[i])
