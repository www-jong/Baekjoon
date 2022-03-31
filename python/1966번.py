from collections import deque
for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    num=a[m]
    q=deque(a)
    s=deque(sorted(a,reverse=True))
    count=deque(list(i for i in range(1,n+1)))
    tmp=0
    gfd=0
    while True:
        g=q.popleft()
        tmp=s.popleft()
        ff=count.popleft()
        if g==tmp:
            gfd+=1
            if (m+1)==ff:
                print(gfd)
                break
        else:
            q.append(g)
            count.append(ff)
            s.appendleft(tmp)
            