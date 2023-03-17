N,M=map(int,input().split())
pac=[]
one=[]
for i in range(M):
    p,s=map(int,input().split())
    p=p if s*6>p else s*6
    pac.append(p)
    one.append(s)
pac.sort()
one.sort()
res=0
res+=(N//6)*pac[0]
N-=(6)*(N//6)
res+=N*one[0] if N*one[0]<pac[0] else pac[0]
print(res)