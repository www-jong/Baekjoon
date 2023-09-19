import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
tree=[0]*(N*4)
def build(node,start,end):
    global tree
    if start==end:
        tree[node]=li[start]
        return
    mid=(start+end)//2
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)
    tree[node]=min(tree[node*2],tree[node*2+1])

def get(st,end,node,left,right):
    if end<left or st>right:
        return 10**10
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    return min(get(st,end,node*2,left,mid),get(st,end,node*2+1,mid+1,right))

def update(st,end,node,idx,val):
    global tree
    if idx<st or end<idx:
        return
    if st==end==idx:
        li[idx]=val
        tree[node]=val
        return
    mid=(st+end)//2
    update(st,mid,node*2,idx,val)
    update(mid+1,end,node*2+1,idx,val)
    tree[node]=min(tree[node*2],tree[node*2+1])


build(1,0,N-1)

for i in range(int(input())):
    c,a,b=map(int,input().split())
    if c==1:
        update(0,N-1,1,a-1,b)
    else:
        print(get(a-1,b-1,1,0,N-1))