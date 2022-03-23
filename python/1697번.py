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
            dis[i]=dis[x]+1
            q.append(i)
            
            
"""
여기서는 dis가 graph의 역할
visited역할은 없음
dis[i]= i번째 왔을때 시간.
이거 잘하면 다이나믹으로도 풀수 있겠다.
"""