n,k=map(int,input().split())
li=[]
tmp=0
for i in range(n):
    now=int(input())
    if k>=now:
        li.append(now)
li.sort(reverse=True)
for i in li:
    tmp+=k//i
    k=k%i
    if k==0:
        break
print(tmp)