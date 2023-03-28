N=int(input())
li=list(map(int,input().split()))
sort_li=sorted(li)
res=[]
for i in li:
    idx=sort_li.index(i)
    res.append(idx)
    sort_li[idx]=-1
print(*res)    
