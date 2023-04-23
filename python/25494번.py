for i in range(int(input())):
    res=0
    a,b,c=map(int,input().split())
    for x in range(1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if x%y==y%z==z%x:
                    res+=1
    print(res)