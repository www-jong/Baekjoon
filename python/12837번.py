import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def build(left,right,node):
    if left==right:
        tree[node]=li[left]
        return
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
    return query(st,end,node*2,left,mid)+query(st,end,node*2+1,mid+1,right)

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]+=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=tree[node*2]+tree[node*2+1]

N,Q=map(int,input().split())
li=[0]*(N)
tree=[0]*(N*4)
build(0,N-1,1)
for i in range(Q):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,N-1,1,b-1,c)
    else:
        print(query(b-1,c-1,1,0,N-1))