import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
stk=[]
res=0
for i in range(N):
    co=0
    while stk:
        if li[stk[-1]]<li[i]:
            res+=1
            stk.pop()
        elif li[stk[-1]]==li[i]:
            pass
        else:
    stk.append(li[i])
    