import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
li=[]
tree=[0]*(4*n)

def maketree(idx,start,end):
    if start==end:
        tree[idx]=li[start]
        return tree[idx]
    mid=start+(end-start)//2
    tree[idx]=maketree(2*idx,start,mid)+maketree(2*idx+1,mid+1,end)
    return tree[idx]

def update(idx,target,val,start,end):
    if target<start or target>end:
        return tree[idx]
    
    if start==end:
        tree[idx]=val
        return tree[idx]
    
    mid=start+(end-start)//2
    tree[idx]=update(idx*2,target,val,start,mid)+update(idx*2+1,target,val,mid+1,end)
    return tree[idx]

def query(idx,start,end,left,right):
    if end<left or start>right:
        return 0

    if start<=left and right<=end:
        return tree[idx]

    mid=left+(right-left)//2
    return query(idx*2,start,end,left,mid)+query(idx*2+1,start,end,mid+1,right)

for i in range(n):
    li.append(int(input()))

maketree(1,0,n-1)

for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,b-1,c,0,n-1)
    else:
        print(query(1,b-1,c-1,0,n-1))
