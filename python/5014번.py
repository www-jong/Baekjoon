from collections import deque
f,s,g,u,d=map(int,input().split())
visit=[10**9 for i in range(f+1)]
q=deque()
q.append(s)
visit[s]=0
ans=-1
while q:
    now=q.popleft()
    if now==g:
        ans=visit[g]
    for i in [u,-d]:
        now2=now+i
        if 1<=now2<=f:
            if visit[now2]>visit[now]+1:
                visit[now2]=visit[now]+1
                q.append(now2)
if ans!=-1:
    print(ans)
else:
    print('use the stairs')