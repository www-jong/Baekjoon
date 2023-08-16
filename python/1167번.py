def func(x,pa):
    global res
    tmp_val=[0]
    
    for k,v in tree[x]:
        if k!=pa:
            tmp_val.append(v+func(k,x))
    tmp_val.sort()
    if len(tmp_val)>=2:
        res=max(res,tmp_val[-1]+tmp_val[-2])
        return tmp_val[-1]
    else:
        return 0
V=int(input())
res=0
tree=[[] for i in range(V+1)]
for i in range(V):
    a,*b,c=map(int,input().split())
    for j in range(len(b)//2):
        tree[a].append((b[j*2],b[j*2+1]))
print(tree,0)
print(func(1,0))
print(res)