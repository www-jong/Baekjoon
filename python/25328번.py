from itertools import combinations
X=input()
Y=input()
Z=input()
k=int(input())
res={}

for i in combinations(X,k):
    if i not in res:
        res[i]=1
    else:
        res[i]+=1
for i in combinations(Y,k):
    if i not in res:
        res[i]=1
    else:
        res[i]+=1
for i in combinations(Z,k):
    if i not in res:
        res[i]=1
    else:
        res[i]+=1

r=[]
for k,v in res.items():
    if v>=2:
        r.append(''.join(list(k)))
if r:
    print(*sorted(r),sep="\n")
else:
    print(-1)