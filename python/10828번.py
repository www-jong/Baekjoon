import sys
q=[]
for i in range(int(input())):
    com=list(sys.stdin.readline().split())
    if com[0]=='push':
        q.append(int(com[1]))
    elif com[0]=='pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif com[0]=='size':
        print(len(q))
    elif com[0]=='empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)