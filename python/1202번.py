import sys,heapq
input=sys.stdin.readline
N,K=map(int,input().split())
bags=[]
sub_ju=[]
ju=[]
for i in range(N):
    M,V=map(int,input().split())
    heapq.heappush(ju,(M,V))

for i in range(K):
    bags.append(int(input()))
bags.sort()
res=0
for bag in bags:
    while ju:
        now_ju=heapq.heappop(ju)
        if now_ju[0]<=bag:
            heapq.heappush(sub_ju,(-now_ju[1],now_ju[1]))
        else:
            heapq.heappush(ju,now_ju)
            break
    if sub_ju:
        res+=heapq.heappop(sub_ju)[1]
print(res)