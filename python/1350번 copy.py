N=int(input())
li=list(map(int,input().split()))
c=int(input())
res=0
for i in li:
    if i%c==0:
        res+=i//c
    else:
        res+=i//c+1
print(res*c)