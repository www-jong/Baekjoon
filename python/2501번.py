n,k=map(int,input().split())
c=0;d=0
for i in range(1,n+1):
    if n%i==0:c+=1
    if c==k:
        print(i)
        d=1
        break
if d==0:print(0)