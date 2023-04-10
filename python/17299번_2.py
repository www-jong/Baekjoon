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

'''
li에서 A의 오등큰수 : 오른쪽에 있으면서 수열 li에서 등장한 횟수가 A보다 크면서 가장 왼쪽에있는 수
    없을경우 오등큰수는 -1

ex) li=[1,1,2,3,4,2,1]
F(1)=3
F(2)=2
F(3)=1
F(4)=1
NGF(0)=-1
NGF(2)=1
NGF(3)=2
NGF(4)=2

555 444 333 22222
'''