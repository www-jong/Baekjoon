import sys
input=sys.stdin.readline

def build(left,right,node):
    global tree
    if left==right:
        tree[node]=li[left]
        return
    mid=(left+right)//2
    build(left,mid,node*2)
    build(mid+1,right,node*2+1)
    tree[node]=min(tree[node*2],tree[node*2+1])

def get(st,end,node,left,right):
    if end<left or right<st:
        return [10**10,10**10]
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    return min(get(st,end,node*2,left,mid),get(st,end,node*2+1,mid+1,right))

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]=[val,idx]
        li[idx]=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=min(tree[node*2],tree[node*2+1])

N=int(input())
t=list(map(int,input().split()))
li=[]
for i in range(N):
    li.append([t[i],i])
tree=[0]*(N*4)
build(0,N-1,1)
for i in range(int(input())):
    c,a,b=map(int,input().split())
    if c==1:
        update(0,N-1,1,a-1,b)
    else:
        v=get(a-1,b-1,1,0,N-1)
        print(v[1]+1)