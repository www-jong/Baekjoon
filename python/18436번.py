import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def build(left,right,node):
    if left==right:
        tree[node]=[1,0] if li[left]%2==0 else [0,1]
        return
    mid=(left+right)//2
    build(left,mid,node*2)
    build(mid+1,right,node*2+1)
    tree[node][0]=tree[node*2][0]+tree[node*2+1][0]
    tree[node][1]=tree[node*2][1]+tree[node*2+1][1]


def query(st,end,node,left,right):
    if end<left or right<st:
        return [0,0]
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    le_val=query(st,end,node*2,left,mid)
    ri_val=query(st,end,node*2+1,mid+1,right)
    return [le_val[0]+ri_val[0],le_val[1]+ri_val[1]]

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]=[1,0] if val%2==0 else [0,1]
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node][0]=tree[node*2][0]+tree[node*2+1][0]
    tree[node][1]=tree[node*2][1]+tree[node*2+1][1]


N=int(input())
li=list(map(int,input().split()))
M=int(input())
tree=[[0,0] for _ in range(N*4)]
build(0,N-1,1)
for _ in range(M):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,N-1,1,b-1,c)
    elif a==2:
        print(query(b-1,c-1,1,0,N-1))
    else:
        print(query(b-1,c-1,1,0,N-1))
