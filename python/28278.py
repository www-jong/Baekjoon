import sys
input=sys.stdin.readline
stk=[]
for m in range(int(input())):
    li=list(map(int,input().split()))
    if len(li)==2:
        if li[0]==1:
            stk.append(li[1])
    elif li[0]==2:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif li[0]==3:
        print(len(stk))
    elif li[0]==4:
        if stk:
            print(0)
        else:
            print(1)
    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)