from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

N,M=map(int,input().split())
graph=[set() for i in range(N+1)]
check={}
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
    if (a,b) not in check:
        check[(a,b)]=c
    else:
        check[(a,b)]=max(check[(a,b)],c)
    if (b,a) not in check:
        check[(b,a)]=c
    else:
        check[(b,a)]=max(check[(b,a)],c)
A,B=map(int,input().split())
res=-1
def bfs(w):
    q=deque()
    q.append(A)
    visit=[0]*(N+1)
    visit[A]=1
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visit[i] and check[(x,i)]>=w:
                visit[i]=1
                q.append(i)
    if visit[B]:
        return 1
    else:
        return 0


st=1
end=1000000000
while st<=end:
    mid=(st+end)//2
    if bfs(mid):
        res=mid
        st=mid+1
    else:
        end=mid-1

print(res)