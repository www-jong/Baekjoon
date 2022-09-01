import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

while True:
    li=list(map(int,input().split()))
    if li[0]==0:
        break
    else:
        n=li[0]
        li.pop(0)
    
    tree=[0]*(n*4)
    mintree=[0]*(n*4)
    maxval=0
    def makemintree(idx,start,end):
        global maxval
        if start==end:
            mintree[idx]=(li[start],li[start])
            return mintree[idx]
        mid=start+(end-start)//2
        left=makemintree(idx*2,start,mid)
        right=makemintree(idx*2+1,mid+1,end)
        mintree[idx]=(min(left[0],right[0]),min(left[0],right[0])*(end-start+1))
        if mintree[idx][1]>maxval:
            maxval=mintree[idx][1]
        return mintree[idx]
    # tree 생성 함수
    def maketree(idx,start,end):
        if start==end:
            tree[idx]=li[start]
            return tree[idx]
        mid=start+(end-start)//2
        tree[idx]=maketree(2*idx,start,mid)+maketree(2*idx+1,mid+1,end)
        return tree[idx]

    # tree에서 구간합 구하는 함수
    def query(idx,start,end,left,right):
        if end<left or start>right:
            return 0

        if start<=left and right<=end:
            return tree[idx]

        mid=left+(right-left)//2
        return query(idx*2,start,end,left,mid)+query(idx*2+1,start,end,mid+1,right)

    maketree(1,0,n-1)
    makemintree(1,0,n-1)
    print(mintree)
    print(maxval)

    '''
    세그먼트 합// 분할정복 하기 
    '''