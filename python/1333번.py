N,L,D=map(int,input().split())
res=0
ch=0
for i in range(1,N+1):
    res+=L
    for j in range(res,res+5):
        if j%D==0:
            res=j
            ch=1
            break
    if ch==1:
        break
print(res)