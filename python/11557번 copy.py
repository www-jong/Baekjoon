for i in range(int(input())):
    a={}
    for i in range(int(input())):
        n,m=input().split()
        a[n]=int(m)
    print(max(a,key=a.get))