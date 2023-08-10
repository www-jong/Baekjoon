from collections import deque
N=int(input())
order=list(map(int,input().split()))
d=deque([i for i in range(1,N+1)])
idx=order[0]
res=[d.popleft()]

while d:
    if idx>0:
        for _ in range(idx-1):
            d.append(d.popleft())
        res.append(d.popleft())
        idx=order[res[-1]-1]
    else:
        for _ in range(-idx-1):
            d.appendleft(d.pop())
        res.append(d.pop())
        idx = order[res[-1]-1]
print(*res)