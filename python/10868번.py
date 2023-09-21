import sys
input=sys.stdin.readline

def build(left,right,node):
    if left==right:
        tree[node]=li[left]
        return
    mid=(left+right)//2
    build(left,mid,node*2)
    build(mid+1,right,node*2+1)
    tree[node]=min(tree[node*2],tree[node*2+1])

def query(st,end,node,left,right):
    if right<st or end<left:
        return 10**11
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    return min(query(st,end,node*2,left,mid),query(st,end,node*2+1,mid+1,right))

N,M=map(int,input().split())
li=[int(input()) for _ in range(N)]
tree=[0]*(N*4)
build(0,N-1,1)
print(tree)
for _ in range(M):
    a,b=map(int,input().split())
    print(query(a-1,b-1,1,0,N-1))
