import sys
input=sys.stdin.readline
def build(node,left,right):
    if left==right:
        tree[node]=[li[left],left]
        return
    mid=(left+right)//2
    build(node*2,left,mid)
    build(node*2+1,mid+1,right)
    if tree[node*2][0]<=tree[node*2+1][0]:
        tree[node]=tree[node*2]
    else:
        tree[node]=tree[node*2+1]
def query(st,end,node,left,right):
    if end<left or st>right:
        return [10**9,10**9]
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    query(st,end,node*2,left,mid)
    query(st,end,node*2+1,mid+1,right)
    if tree[node*2][0]<=tree[node*2+1][0]:
        return tree[node*2]
    else:
        return tree[node*2+1]
def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==idx==right:
        li[idx]=val
        tree[node]=[val,idx]
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    if tree[node*2][0]<=tree[node*2+1][0]:
        tree[node]=tree[node*2]
    else:
        tree[node]=tree[node*2+1]
N=int(input())
li=list(map(int,input().split()))
tree=[[0,0] for i in range(N*4)]
build(1,0,N-1)
for _ in range(int(input())):
    q=[*map(int,input().split())]
    if len(q)==1:
        print(query(0,N-1,1,0,N-1)[1]+1)
    else:
        a,b,c=q
        update(0,N-1,1,b-1,c)