def div(v):
    if v>0:
        return 1
    elif v==0:
        return 0
    else:
        return -1
def build(node,left,right):
    if left==right:
        tree[node]=div(li[left])
        return
    mid=(left+right)//2
    build(node*2,left,mid)
    build(node*2+1,mid+1,right)
    tree[node]=div(tree[node*2]*tree[node*2+1])

def sign(st,end,node,left,right):
    if end<left or right<st:
        return 1
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    return div(sign(st,end,node*2,left,mid)*sign(st,end,node*2+1,mid+1,right))

def update(left,right,node,idx,val):
    if idx<left or right<idx:
        return
    if left==right==idx:
        tree[node]=div(val)
        return
    mid=(left+right)//2
    update(left,mid,node*2,idx,val)
    update(mid+1,right,node*2+1,idx,val)
    tree[node]=div(tree[node*2]*tree[node*2+1])

while True:
    try:
        N,K=map(int,input().split())
        li=list(map(int,input().split()))
        tree=[0]*(N*4)
        build(1,0,N-1)
        res=''
        for i in range(K):
            c,a,v=input().split()
            if c=='C':
                update(0,N-1,1,int(a)-1,int(v))
            else:
                tmp=sign(int(a)-1,int(v)-1,1,0,N-1)
                if tmp>0:
                    res+='+'
                elif tmp==0:
                    res+='0'
                else:
                    res+='-'
        print(res)
    except EOFError:
        break
