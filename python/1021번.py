from collections import deque
n,m=map(int,input().split())
li=deque([i for i in range(1,n+1)])
findnum=list(map(int,input().split()))
count=0
for i in findnum:
    d=-li.index(i) if li.index(i)<=(len(li)-li.index(i)) else len(li)-li.index(i)
    li.rotate(d)
    li.popleft()
    count+=abs(d)
print(count)    
