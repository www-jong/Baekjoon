import sys
n,m=map(int,sys.stdin.readline().split())
a=[0]+list(map(int,sys.stdin.readline().split()))
d=[0]*(n+1)
d[1]=a[1]
for i in range(2,n+1):
    d[i]=d[i-1]+a[i]
for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    print(d[y]-d[x-1])