import sys,heapq
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    heapq.heappush(li,int(input()))
res=0
for i in range(1,N):
    a,b=heapq.heappop(li),heapq.heappop(li)
    res+=a+b
    heapq.heappush(li,a+b)
print(res)
