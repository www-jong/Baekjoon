a=0;b=0
for i in range(5):
    if (c:=sum(map(int,input().split())))>b:
        b=c
        a=i+1
print("%d %d"%(a,b))