import sys
import heapq as hq
input=sys.stdin.readline
for _ in range(int(input())):
    max_q=[]
    min_q=[]
    check=[0]*1000001
    for i in range(int(input())):
        a,b=input().split()
        b=int(b)
        if a=="I":
            hq.heappush(min_q,(b,i))
            hq.heappush(max_q,(-b,i))
            check[i]=1
        else:
            if b==1:
                while max_q and not check[max_q[0][1]]:
                    hq.heappop(max_q)
                if max_q:
                    check[max_q[0][1]]=0
                    hq.heappop(max_q)
            else:
                while min_q and not check[min_q[0][1]]:
                    hq.heappop(min_q)
                if min_q:
                    check[min_q[0][1]]=0
                    hq.heappop(min_q)
    while min_q and not check[min_q[0][1]]:hq.heappop(min_q)
    while max_q and not check[max_q[0][1]]:hq.heappop(max_q)
    if min_q and max_q:
        print(-max_q[0][0],min_q[0][0])
    else:
        print("EMPTY")