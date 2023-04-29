import sys
input=sys.stdin.readline

N=int(input())
li=[int(input()) for i in range(N)]
stk=[]
for i in range(N):
    while stk:
        if stk[-1]<=li[i]:
            stk.pop()
        else:
            break
    stk.append(li[i])
print(len(stk))        