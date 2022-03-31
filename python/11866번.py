from collections import deque
n,k=map(int,input().split())
a=deque(list(i for i in range(1,n+1)))
s=[]
k-=1
while a:
    a.rotate(-k)
    s.append(a.popleft())
print("<",end="")
print(*s,sep=", ",end="")
print(">")
