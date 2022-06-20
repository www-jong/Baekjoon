from collections import deque
import sys
input=sys.stdin.readline
cl=deque(list(input().rstrip()))
cr=deque()
for i in range(int(input())):
    com=input().rstrip()
    if com=="L":
        if len(cl)!=0:
            cr.appendleft(cl.pop())
    elif com=="D":
        if len(cr)!=0:
            cl.append(cr.popleft())
    elif com=="B":
        if len(cl)!=0:
            cl.pop()
    else:
        cl.append(com[-1])
for i in cl:
    print(i,end="")
for i in cr:
    print(i,end="")