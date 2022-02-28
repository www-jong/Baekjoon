for _ in range(int(input())):
    a1,a2=map(int,input().split());c=0
    if a1>a2:a=a1;b=a2
    else:a=a2;b=a1
    def func(a,b):       
        while b!=0:
            c=a%b
            a=b
            b=c
        return a
    print(int(a*b/func(a,b)))