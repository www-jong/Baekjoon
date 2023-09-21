import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def build(left,right,node):
    if left==right:
        tree[node]=li(left)
    mid=(left+right)//2
    build(left,mid,node*2)
    build(mid+1,right,node*2+1)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(st,end,node,left,right):
    if end<left or right<st:
        return 0
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    left_val=query(st,end,node*2,left,mid)
    right_val=query(st,end,node*2+1,mid+1,right)
    return left_val+right_val

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return 0
    if left==right==idx:
        tree[node]=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=tree[node*2]+tree[node*2+1]

N,M=map(int,input().split())
li=[0]*(N)
tree=[0]*(N*4)
for i in range(M):
    a,b,c=map(int,input().split())
    if not a:
        b,c=min(b,c),max(b,c)
        print(query(b-1,c-1,1,0,N-1))
    else:
        update(0,N-1,1,b-1,c)
