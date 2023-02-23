N,M=map(int,input().split())
li=[i for i in range(N+1)]
for i in range(M):
    i,j,k=map(int,input().split())
    li[i:j+1]=li[k:j+1]+li[i:k]
print(*li[1:])