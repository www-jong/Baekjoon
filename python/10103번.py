a=b=100
for i in range(int(input())):
    n,m=map(int,input().split())
    if n>m:b-=n
    elif n<m:a-=m
print("%d\n%d"%(a,b))