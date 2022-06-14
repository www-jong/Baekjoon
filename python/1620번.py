import sys
n,m=map(int,sys.stdin.readline().split())
l={}
for i in range(n):
    s=sys.stdin.readline().strip()
    l[s]=i+1
    l[str(i+1)]=s
for i in range(m):
    print(l[sys.stdin.readline().strip()])
    