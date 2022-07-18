from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int,input().split()))
check=[-1]*(n)
i=0
ch=0
while i<=n:
    co,ch=1,0
    for j in range(i+1,n):
        if li[j]>li[i]:
            for m in range(i,i+co):
                check[m]=li[j]
            ch=1
            break
        else:
            co+=1
    if ch==1:
        i+=co
    else:
        i+=1
print(*check)