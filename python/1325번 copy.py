from collections import deque
import sys
def bfs(gr,v,s):
 q,c,v[s]=deque(),0,1
 q.append(s)
 while q:
  d=q.popleft()
  for i in gr[d]:
   if v[i]==0:
    q.append(i)
    v[i]=1
    c+=1
 return c
n,m=map(int,sys.stdin.readline().split())
gr=[[] for i in range(n+1)]
v=[0]*(n+1)
for i in range(m):
 a,b=map(int,sys.stdin.readline().split())
 gr[b].append(a)
ma,an=-10,[]
for i in range(1,n+1):
 v2=v.copy()
 g=bfs(gr,v2,i)
 if g>ma:
  an.clear()
  an.append(i)
  ma=g
 elif g==ma:
  an.append(i)
print(*an)