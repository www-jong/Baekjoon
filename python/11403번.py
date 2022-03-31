n=int(input())
ans=[[0]*(n+1)]
for i in range(n):
    ans.append([0]+list(map(int,input().split())))
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if ans[a][k]==1 and ans[k][b]==1:
                ans[a][b]=1
for i in range(1,n+1):
    print(*ans[i][1:],sep=" ")