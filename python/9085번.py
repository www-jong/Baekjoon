for i in range(int(input())):
    res=0
    _=input()
    li=list(map(int,input().split()))
    for z in li:
        res+=z
    print(res)