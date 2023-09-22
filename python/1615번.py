import sys
input=sys.stdin.readline

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
    if idx==left==right:
        tree[node]+=val
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=tree[node*2]+tree[node*2+1]

N,M=map(int,input().split())
li=[]
tree=[0]*(N*4)
g={}
for i in range(M):
    a,b=map(int,input().split())
    if a not in g:
        g[a]=[b]
    else:
        g[a].append(b)
#print(tree)
res=0
for a in sorted(g.keys()):
    for b in sorted(g[a]):
        update(0,N-1,1,b-1,1)
        res+=query(b,N-1,1,0,N-1)
    #print(tree)
print(res)
