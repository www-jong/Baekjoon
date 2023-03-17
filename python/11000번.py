import sys,heapq
input=sys.stdin.readline
N=int(input())
min_t=10**9
hp=[]
li=[]

for i in range(N):
    s,e=map(int,input().split())
    li.append([s,e])
li.sort()
heapq.heappush(hp,li[0][1])
for i in range(1,len(li)):
    if li[i][0]>=hp[0]:
        heapq.heappop(hp)
        heapq.heappush(hp,li[i][1])
    else:
        heapq.heappush(hp,li[i][1])
print(len(hp))