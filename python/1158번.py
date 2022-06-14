from collections import deque
n,k=map(int,input().split())
q=deque([i for i in range(1,n+1)])
li2=[]
while q:
    q.rotate(-(k-1))
    li2.append(q.popleft()) 
print("<",end="")
print(*li2,sep=", ",end="")
print(">")