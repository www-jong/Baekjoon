an,am=map(int,input().split())
a=[]
for i in range(an):
    tmp=list(map(int,input().split()))
    a.append(tmp)
bn,bm=map(int,input().split())
b=[]
for i in range(bn):
    tmp=list(map(int,input().split()))
    b.append(tmp)
    
def func(li1,li2,j):
    res=0
    tmpli2=[]
    for i in range(bn):
        tmpli2.append(li2[i][j])
    for i in range(len(li1)):
        res+=li1[i]*tmpli2[i]
    return res
c=[[0]*(bm) for i in range(an)]
for i in range(an):
    for j in range(bm):
        c[i][j]=func(a[i],b,j)
for i in range(an):
    print(*c[i])