import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def maketree(idx,start,end):
    global maxval
    if start==end:
        tree[idx]=start
        return tree[idx]
    mid=start+(end-start)//2
    left=maketree(idx*2,start,mid)
    right=maketree(idx*2+1,mid+1,end)
    tree[idx]=left if li[left]<li[right] else right
    return tree[idx]
'''
# tree 생성 함수
def maketree(idx,start,end):
    global maxval
    if start==end:
        tree[idx]=(start,start,start,li[start])
        return tree[idx]
    mid=start+(end-start)//2
    left=maketree(idx*2,start,mid)
    right=maketree(idx*2+1,mid+1,end)
    tree[idx]=(start,end,left[2] if left[3]<right[3] else right[2],min(left[3],right[3]))
    if tree[idx][1]>maxval:
        maxval=tree[idx][1]
    return tree[idx]
# 분할정복(특정 구간 안에서 좌우를 비교)
def query(idx,start,end,left,right):
    if end<left or start>right:
        return 0

    if start<=left and right<=end:
        return tree[idx]

    mid=left+(right-left)//2
    return query(idx*2,start,end,left,mid)+query(idx*2+1,start,end,mid+1,right)
'''

# 트리연산(특정 구간에서 최소값인덱스 알아내기)
def query(idx,start,end,left,right):
    if end<left or start>right:
        return -1

    if start<=left and right<=end:
        return tree[idx]

    mid=left+(right-left)//2
    left_vals=query(idx*2,start,end,left,mid)
    right_vals=query(idx*2+1,start,end,mid+1,right)
    if left_vals!=-1 and right_vals!=-1:
        return left_vals if li[left_vals]<li[right_vals] else right_vals
    elif left_vals!=-1 and right_vals==-1:
        return left_vals
    elif left_vals==-1 and right_vals!=-1:
        return right_vals
    #return query(idx*2,start,end,left,mid) if query(idx*2,start,end,left,mid)[3] < query(idx*2+1,start,end,mid+1,right)[3] else query(idx*2+1,start,end,mid+1,right)

def func(start,end,left,right,val=0):

    if start==end:
        return max(li[start],val)
    elif start>end:
        return val
    print(f"start:{start},end:{end} val:{val}")
    # 구간내 최소값 인덱스
    center=query(1,start,end,left,right)
    
    left_val=func(start,center-1,left,right,val)
    right_val=func(center+1,end,left,right,val)
    center_val=(end-start+1)*(li[center])

    return max(left_val,right_val,center_val)
    

def minimi(start,end,type=0):
    minidx=start
    minval=10**9
    
    for i in range(start,end+1):
        if li[i]<minval:
            minval=li[i]
            minidx=i
    if type==1:
        return minval
    else:
        return minidx
    
while True:
    li=list(map(int,input().split()))
    if li[0]==0:
        break
    else:
        n=li.pop(0)
    
    tree=[0]*(n*4)
    maxval=0
    minval=10**9
    minidx=0
    for i,j in enumerate(li):
        if j<minval:
            minval=j
            minidx=i
    maketree(1,0,n-1)
    print(tree)
    print('maxval : %d'%(maxval))
    print('query val : %d'%(func(0,n-1,0,n-1)))
    #print(query(1,0,n-1,0,n-1))
    '''
    세그먼트 합// 분할정복 하기 
    tree : [(시작인덱스,끝인덱스,최소값인덱스,최소값,)]

    분할정복
    query(구간시작,구간끝,인덱스(구간을 나누는 인덱스))
    '''