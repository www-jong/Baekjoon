import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
N=int(input())
in_order=list(map(int,input().split()))
post_order=list(map(int,input().split()))
tree=[0]*(N+1)
for i in range(N):
    tree[in_order[i]]=i

def divide(in_st,in_end,post_st,post_end):
    if in_st>in_end or post_st>in_end:
        return
    root=post_order[post_end]
    left=tree[root]-in_st
    right=in_end-tree[root]
    print(root,end=" ")
    divide(in_st,in_st+left-1,post_st,post_st+left-1)
    divide(in_end-right+1,in_end,post_end-right,post_end-1)
divide(0,N-1,0,N-1)