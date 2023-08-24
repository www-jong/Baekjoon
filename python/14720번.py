N=int(input())
li=[*map(int,input().split())]
r,c=0,-1
for i in li:
    if c==-1 and i==0:
        r+=1
        c=0
    elif c==0 and i==1:
        r+=1
        c=1
    elif c==1 and i==2:
        r+=1
        c=2
    elif c==2 and i==0:
        r+=1
        c=0
print(r)