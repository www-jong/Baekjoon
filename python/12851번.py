from collections import deque
n,k=map(int,input().split())
dis=[0]*100001

q=deque()
q.append(n)
while q:
    x=q.popleft()
    if x==k:
        print(dis[x])
        break
    for i in (x-1,x+1,x*2):
        if 0<=i<=100000 and not dis[i]:
            if i!=0 and i==x*2:
                dis[i]=dis[x]
                q.appendleft(i)
            else:
                dis[i]=dis[x]+1
                q.append(i)
            