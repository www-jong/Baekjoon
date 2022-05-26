best=-1
for i in range(int(input())):
    a=list(map(int,input().split()))
    if len(set(a))==1:
        best=10000+1000*a[0]
    else:
        for i in range(3):
            