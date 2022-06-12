import sys
sys.setrecursionlimit(10**9)

n=int(sys.stdin.readline())
tree=[[] for i in range(n+1)]
ans=[-1]*(n+1)
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
def func(n):
    for i in tree[n]:
        if ans[i]==-1:
            ans[i]=n
            func(i)
func(1)
print(*ans[2:],sep="\n")