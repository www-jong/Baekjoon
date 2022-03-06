t=int(input())
a=0;b=0;c=0;d=0
if t%10!=0:
    print("-1")
else:
    if (d:=(t//300))>=1:
        t-=300*d
        a+=d
    if (d:=(t//60))>=1:
        t-=60*d
        b+=d
    if (d:=(t//10))>=1:
        t-=10*d
        c+=d
    print("%d %d %d"%(a,b,c))