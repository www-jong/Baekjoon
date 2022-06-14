from collections import deque
import sys
q=deque()
for i in range(int(sys.stdin.readline())):
    com=list(map(str,sys.stdin.readline().split()))
    if len(com)==2:
        if com[0][-1]=="t":
            q.appendleft(int(com[1]))
        else:
            q.append(int(com[1]))
    else:
        if com[0]=="pop_front":
            print(q.popleft() if len(q)!=0 else -1)
        elif com[0]=="pop_back":
            print(q.pop() if len(q)!=0 else -1)
        elif com[0]=="size":
            print(len(q))
        elif com[0]=="empty":
            print(1 if len(q)==0 else 0)
        elif com[0]=="front":
            print(q[0] if len(q)!=0 else -1)
        else:
            print(q[-1] if len(q)!=0 else -1)
        