import heapq
n,m=map(int,input().split())
li=list(map(int,input().split()))
heapq.heapify(li)
res=0
for i in range(m):
    a,b=heapq.heappop(li),heapq.heappop(li)
    heapq.heappush(li,(a+b))
    heapq.heappush(li,(a+b))
print(sum(li))