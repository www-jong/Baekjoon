import sys,bisect
sys.setrecursionlimit(10**9)
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
li.sort()
def getrope(num):
    start=bisect.bisect_left(li,num)
    re=0
    for i in range(start,k):
        re+=li[i]//num
    return re

while min<=max:
    val=getrope((min+max)//2)
    if val<n:
        max=(min+max)//2-1
    else:
        min=(min+max)//2+1
print(max)