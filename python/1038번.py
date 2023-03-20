from itertools import combinations
N=int(input())
li=[]
if N>1022:
    print(-1)
else:
    for i in range(1,11):
        for comb in combinations(range(0,10),i):
            comb=sorted(list(comb),reverse=True)
            li.append(int(''.join(map(str,comb))))
    li.sort()
    print(li[N])
            
