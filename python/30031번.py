N=int(input())
c=[136,142,148,154]
d=[1,5,10,50]
r=0
for _ in range(N):
    a,b=map(int,input().split())
    for i in range(4):
        if a%c[i]==0:
            r+=a//c[i]*(b//68)*d[i]*1000
            break
print(r)