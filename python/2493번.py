import sys
sys.setrecursionlimit(10000000)
N=int(input())
li=[0]+list(map(int,input().split()))
stk=[]
res=[0]*(N+1)
stk.append((1,li[1]))
for i in range(2,N+1):
    c=i
    while stk:
        idx,now=stk.pop()
        if li[i]<=now:
            res[i]=idx
            stk.append((idx,now))
            break
    stk.append((i,li[i]))
print(*res[1:])
