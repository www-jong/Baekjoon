n,k=map(int,input().split())
quest=list(map(int,input().split()))
quest.sort()
res=0
idx=1
for i in quest[1:]:
    res+=i*idx
    if idx<k:
        idx+=1
print(res)