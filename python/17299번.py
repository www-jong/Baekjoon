import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
li2=[0]*(max(li)+1)
res=[-1]*(len(li))
stk=[]
for i in li:
    li2[i]+=1
for i in range(N):
    while stk:
        if li2[li[stk[-1]]]<li2[li[i]]:
            res[stk.pop()]=li[i]
        else:
            break
    stk.append(i)
print(*res)