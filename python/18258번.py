import sys
from collections import deque
input=sys.stdin.readline
li=deque()
for i in range(int(input())):
    com=list(input().split())
    if len(com)!=1:
        li.append(int(com[1]))
    else:
        if com[0]=='pop':
            if len(li)!=0:
                print(li.popleft())
            else:
                print('-1')
        elif com[0]=='size':
            print(len(li))
        elif com[0]=='empty':
            if len(li)!=0:
                print(0)
            else:
                print(1)
        elif com[0]=='front':
            if len(li)!=0:
                print(li[0])
            else:
                print('-1')
        elif com[0]=='back':
            if len(li)!=0:
                print(li[-1])
            else:
                print('-1')