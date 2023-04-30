N=int(input())
li=list(map(int,input().split()))
res=0
for i in li:
    if i<=N:
        res+=i
    else:
        res+=N
print(res)