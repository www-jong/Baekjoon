N=int(input())
li=list(map(int,input().split()))
res=0
maxs=0
idx=0
for i in li:
    if i>maxs:
        maxs=i
        idx=0
    else:
        idx+=1
    res=max(res,idx)
print(res)
