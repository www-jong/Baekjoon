import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def maketree(idx,start,end):
    if start==end:
        tree[idx]=start
        return tree[idx]
    mid=start+(end-start)//2
    left=maketree(idx*2,start,mid)
    right=maketree(idx*2+1,mid+1,end)
    tree[idx]=left if li[left]<li[right] else right
    return tree[idx]

def query(idx,start,end,left,right):
    if end<left or start>right:return -1
    if start<=left and right<=end:return tree[idx]
    mid=left+(right-left)//2
    left_vals=query(idx*2,start,end,left,mid)
    right_vals=query(idx*2+1,start,end,mid+1,right)
    if left_vals!=-1 and right_vals!=-1:
        if li[left_vals]==li[right_vals]:
            mid=end-start
            return left_vals if abs(mid-left_vals)<abs(mid-right_vals) else right_vals
        else:    
            return left_vals if li[left_vals]<li[right_vals] else right_vals
    elif left_vals!=-1 and right_vals==-1:
        return left_vals
    elif left_vals==-1 and right_vals!=-1:
        return right_vals

def func(start,end,left,right,val=0):
    if start==end:return max(li[start],val)
    elif start>end:return val
    center=query(1,start,end,left,right)
    left_val=func(start,center-1,left,right,val)
    right_val=func(center+1,end,left,right,val)
    center_val=(end-start+1)*(li[center])
    return max(left_val,right_val,center_val)
        
while True:
    li=list(map(int,input().split()))
    if li[0]==0:break
    else:n=li.pop(0)
    tree=[0]*(n*4)
    maketree(1,0,n-1)
    print(func(0,n-1,0,n-1))