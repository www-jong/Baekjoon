N=int(input())
li=list(map(int,input().split()))
tmp=[0]*N
res=0

for i in range(N):
    if li[i]!=tmp[i]:
        res+=1
        tmp[i]=not tmp[i]
        if i+1<N:
            tmp[i+1]=not tmp[i+1]
        if i+2<N:
            tmp[i+2]=not tmp[i+2]
print(res)