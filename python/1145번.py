li=list(map(int,input().split()))
res=10000000000
tmp=10**9
for i in li:
    for j in range(1,200):
        ch=0
        t=i*j
        for z in li:
            if t%z==0:
                ch+=1
            if ch==3:
                tmp=min(tmp,t)
                break
print(tmp)