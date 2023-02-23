N,M=map(int,input().split())
li=[i for i in range(N+1)]
for _ in range(M):
    i,j=map(int,input().split())
    li[i:j+1]=li[j:i-1:-1]
print(*li[1:])