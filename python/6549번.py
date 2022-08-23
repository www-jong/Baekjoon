import sys
def func(st,end,idx):
    if st==end:
        tree[idx]=li[st]
        return tree[idx]
    mid=(st+end)//2
    tree[idx]=func(st,mid,idx*2)+func(mid+1,end,idx*2+1)
    return tree[idx]
def func_sum(st,end,idx,left,right):
    if left>end or right<st:
        return 0
    if left<=st and right>=end:
        return tree[idx]
    mid=(st+end)//2
    return func_sum(st,mid,idx*2,left,right)+func_sum(mid+1,end,idx*2+1,left,right)

while True:
    li=list(map(int,sys.stdin.readline().rstrip().split()))
    if li[0]==0:
        break
    tree=[0]*(li[0]*4)
    li_sum=[0]*len(li)
    func(1,li[0],1)
    print(tree)

'''
세그먼트 트리로 각 구간의 합을 구한 뒤,
각 구간의 최솟값*구간의..... 뭐여
'''