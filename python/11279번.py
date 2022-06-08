import sys
import heapq
heaps=[]
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if n==0:
        if len(heaps)==0:
            print(0)
        else:
            print(heapq.heappop(heaps)[1])
    else:
        heapq.heappush(heaps,(-n,n))