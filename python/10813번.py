N,M=map(int,input().split())
li=[i for i in range(1,N+1)]
for i in range(M):
    i,j=map(int,input().split())
    li[i-1],li[j-1]=li[j-1],li[i-1]
print(*li)