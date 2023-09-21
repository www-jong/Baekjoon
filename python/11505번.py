import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def build(node,left,right):
    if left==right:
        tree[node]=li[left]
        return
    mid=(left+right)//2
    build(node*2,left,mid)
    build(node*2+1,mid+1,right)
    tree[node]=tree[node*2]*tree[node*2+1]% 1000000007


def query(st,end,node,left,right):
    if end<left or st>right:
        return 1
    if st<=left and right<=end:
        return tree[node]% 1000000007
    mid=(left+right)//2
    return query(st,end,node*2,left,mid)*query(st,end,node*2+1,mid+1,right)% 1000000007

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]=val
        li[idx]=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=tree[node*2]*tree[node*2+1]%1000000007


N,M,K=map(int,input().split())
li=[int(input()) for _ in range(N)]
tree=[0]*(N*4)
build(1,0,N-1)
for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,N-1,1,b-1,c)
    else:
        print(query(b-1,c-1,1,0,N-1)%1000000007)