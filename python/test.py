from itertools import combinations
n=30
res=0

res2=0
tmp_li=[i for i in range(n)]
for i in range(1,n+1):
    res2+=len(list(combinations(tmp_li,i)))
print(f'res2 : {res2}')