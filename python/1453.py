N=int(input())
li=list(map(int,input().split()))
tmp=[0 for i in range(101)]
res=0
for i in li:
    if tmp[i]==0:
        tmp[i]=1
    else:
        res+=1
print(res)
