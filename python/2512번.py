N=int(input())
li=sorted(list(map(int,input().split())))
M=int(input())
st,end,mid=0,li[-1],0
def f(x):
    t=0
    for i in li:
        if i<x:
            t+=x-i
        else:
            break
    return t
while st<=end:
    mid=(st+end)//2
    g=f(mid)
    if mid*N-g==M:
        break
    elif mid*N-g<M:
        st=mid+1
    else:
        end=mid-1
for i in range(3,-3,-1):
    now=mid+i
    if now*N-f(now)<=M and now<=li[-1]:
        print(now)
        break