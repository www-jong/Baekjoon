def tu(x):
    return abs(int(x))
N,M=map(int,input().split())
li=list(map(tu,input().split()))
m=set(li)
res=-(10**8)
for _ in range(M-1):
    t=set()
    for i in m:
        for j in li:
            t.add(i^j)
    m=t
print(max(m))