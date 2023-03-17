import sys
n=10000
so=[0]*(10000)
l=[1]*(n+1)
nu=0
for i in range(2,n+1):
 if l[i]==1:so[nu]=i;nu+=1
 l[i::i]=[0]*(n//i)
so=set(so)
for i in range(int(input())):
    n=int(sys.stdin.readline())
    mi=0
    ma=0
    mm=n
    for m in so:
        if n-m in so:
            if abs(n-2*m)<mm:
                if m<n-m:
                    mi=m
                    ma=n-m
                else:
                    mi=n-m
                    ma=m
                mm=abs(n-2*m)
    print("%d %d"%(mi, ma))
