import sys
input=sys.stdin.readline
def build(node,left,right):
    if left==right:
        tree[node]=li[left]
        return
    mid=(left+right)//2
    build(node*2,left,mid)
    build(node*2+1,mid+1,right)
    tree[node]=max(tree[node*2],tree[node*2+1])

def query(st,end,node,left,right):
    if end<left or right<st:
        return 0
    if st<=left and right<=end:
        return tree[node]
    mid=(left+right)//2
    return max(query(st,end,node*2,left,mid),query(st,end,node*2+1,mid+1,right))
T=int(input())
for _ in range(T):
    r=1
    N=int(input())
    tree=[0]*(N*4)

    li=list(map(int,input().split()))
    build(1,0,N-1)
    dic={}
    c=[0]*max(li)
    for i in range(N):
        if li[i] not in dic:
            dic[li[i]]=[i]
        else:
            dic[li[i]].append(i)
    for i in set(li):
        if len(dic[i])==1:
            continue
        if query(min(dic[i]),max(dic[i]),1,0,N-1)>i:
            r=0
            break

    print("Yes" if r==1 else "No")