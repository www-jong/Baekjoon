for i in range(int(input())):
    li=list(map(int,input().split()))
    tmp=0
    mins=1000000
    for i in li:
        if i%2==0:
            tmp+=i
            mins=min(i,mins)
    print(tmp,mins)