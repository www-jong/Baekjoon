a=[]
b=[0 for _ in range(8001)]
n=int(input())
mi=4000
res=[0,0,0,0]
for i in range(n):
    s=int(input())
    a+=[s]
    b[s+4000]+=1
    if mi>s:
        mi=s
res[0]=round(sum(a)/n)
a.sort()
res[1]=a[n//2]
li=list(filter(lambda x:b[x]==max(b),range(len(b))))
if len(li)==1:
    res[2]=b.index(max(b))-4000
else:
    res[2]=li[1]-4000 
c=list(set(a))
c.sort()
res[3]=max(c)-mi
for i in range(4):
    print(res[i])