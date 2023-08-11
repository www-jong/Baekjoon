from time import time
from collections import deque
import sys
ipnut=sys.stdin.readline
st_time=time()
def D(x):
    x=x*2%10000
    return x
def S(x):
    x=9999 if x==0 else x-1
    return x
def L(n):
    return n%1000*10+n//1000
def R(n):
    return n%10*1000+n//10

d={0:D,1:S,2:L,3:R}
g='DSLR'
for _ in range(int(input())):
    A,B=map(int,input().split())
    visit=[[] for i in range(10000)]
    visit[A]=[]
    q=deque()
    q.append(A)
    while q:
        val=q.popleft()
        if val==B:
            sys.stdout.write("".join(visit[B]) + "\n")
            break
        for i in range(4):
            n_val=d[i](val)
            if not visit[n_val]:
                visit[n_val]=(visit[val]if val!=A else[])+[g[i]]
                q.append((n_val))
print(time()-st_time)