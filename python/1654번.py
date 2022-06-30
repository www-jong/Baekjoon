import sys
input=sys.stdin.readline
k,n=map(int,input().split())
min=1
max=0
li=[]
for i in range(k):
    tmp=int(input())
    li.append(tmp)
    if tmp>max:
        max=tmp
while min<=max:
    mid=(min+max)//2
    val=0
    for i in li:
        val+=i//mid
    if val>=n:
        min=mid+1
    else:
        max=mid-1
print(min)