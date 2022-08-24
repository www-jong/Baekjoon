import sys
input=sys.stdin.readline
n,m=map(int,input().split())
li=list(map(int,input().split()))
st,end=min(li),max(li)
while st<=end:
    mid=(st+end)//2
    ans=0
    for i in li:
        if i>mid:
            ans+=i-mid
    if ans>=m:
        st=mid+1
    else:
        end=mid-1
print(end)

