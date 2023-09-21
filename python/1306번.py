import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def build(left,right,node):
    if left==right:
        tree[node]=li[left]
        return
    mid=(left+right)//2
    build(left,mid,node*2)
    build(mid+1,right,node*2+1)
    tree[node]=max(tree[node*2],tree[node*2+1])

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=max(tree[node*2],tree[node*2+1])

N,M=map(int,input().split())
li=list(map(int,input().split()))+[0]*M
idx=0
tree=[0]*((2*(M))*4)
build(0,2*M-2,1)
res=[]
res.append(tree[1])
for i in range(M*2-1,N):
    print('idx',i,li[i])
    update(0,2*(M-1),1,idx,li[i])
    idx+=1
    if idx==(2*(M-1)+1):
        idx=0
    res.append(tree[1])
print(*res,sep=" ")