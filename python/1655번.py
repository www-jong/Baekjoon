import sys,heapq
input=sys.stdin.readline
lq=[]
rq=[]
n=1
ans=[]
mid=-1
rmin=20000
lmax=-20000
for i in range(int(input())):
    s=int(input())
    ll=len(lq)
    rl=len(rq)
    if ll>0 and rl>0:
        rmin=rq[0]
        lmax=lq[0][1]
    if n==1:
        mid=s
        heapq.heappush(lq,(-s,s))
        lmax=s
    else:
        if ll==rl:
            if rmin<s:
                g=heapq.heappop(rq)
                heapq.heappush(lq,(-g,g))
                heapq.heappush(rq,s)
                rmin=s
            else:
                heapq.heappush(lq,(-s,s))
        else:
            if s<lmax:
                g=heapq.heappop(lq)[1]
                heapq.heappush(rq,g)
                heapq.heappush(lq,(-s,s))
            else:
                heapq.heappush(rq,s)
    mid=lq[0][1]
    print(mid)
    n+=1



'''
1 2 3 4 5    8 9 10 11
- 2
2  2   5
1

-10
2     5
1     10

'''
