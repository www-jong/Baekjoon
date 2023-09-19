import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
N,M=map(int,input().split())
li=[int(input()) for i in range(N)]
question=[list(map(int,input().split())) for i in range(M)]

maxtree=[0]*(N*4)
mintree=[0]*(N*4)
def maxbuild(node,left,right):
    global maxtree
    if left==right:
        maxtree[node]=li[left]
        return
    mid=(left+right)//2
    maxbuild(2*node,left,mid)
    maxbuild(2*node+1,mid+1,right)
    maxtree[node]=max(maxtree[node*2],maxtree[node*2+1])

def minbuild(node,left,right):
    global mintree
    if left==right:
        mintree[node]=li[left]
        return
    mid=(left+right)//2
    minbuild(2*node,left,mid)
    minbuild(2*node+1,mid+1,right)
    mintree[node]=min(mintree[node*2],mintree[node*2+1])


def maxquery(start,end,node,left,right):
    if end<left or start>right:
        return 0
    if start<=left and right<=end:
        return maxtree[node]
    mid=(left+right)//2
    return max(maxquery(start,end,2*node,left,mid),maxquery(start,end,2*node+1,mid+1,right))

def minquery(start,end,node,left,right):
    if end<left or start>right:
        return 10**10
    if start<=left and right<=end:
        return mintree[node]
    mid=(left+right)//2
    return min(minquery(start,end,2*node,left,mid),minquery(start,end,2*node+1,mid+1,right))

maxbuild(1,0,N-1)
minbuild(1,0,N-1)
for x,y in question:
    print(minquery(x-1,y-1,1,0,N-1),maxquery(x-1,y-1,1,0,N-1))