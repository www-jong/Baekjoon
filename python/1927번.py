import heapq,sys
h=[]
for i in range(int(sys.stdin.readline())):
    x=int(sys.stdin.readline())
    if x==0:
        print(heapq.heappop(h) if len(h)!=0 else 0)
    else:
        heapq.heappush(h,x)
