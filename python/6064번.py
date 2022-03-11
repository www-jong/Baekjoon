for i in range(int(input())):
    M,N,x,y=map(int,input().split())
    a=0;b=0
    count=0
    check=0
    while a!=x or b!=y:
        if a<M:a+=1
        else:a=1
        if b<N:b+=1
        else:b=1
        count+=1
        if count>(M-1)*(N-1):
            check=1
            break
    if check==0:
        print(count)
    else:
        check=0
        print(-1)