N,K=map(int,input().split())
li=[0]
res=''
stk=[]
for i in input():
    li.append(int(i))
for i in range(1,N+1):
    if K==0:
        stk.append(li[i])
    else:
        while stk:
            if K==0:
                break
            if li[i]>stk[-1]:
                stk.pop()
                K-=1
            else:
                break
        stk.append(li[i])
if K!=0:
    while K!=0:
        stk.pop()
        K-=1
print(*stk,sep="")