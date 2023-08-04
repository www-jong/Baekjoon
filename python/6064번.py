for i in range(int(input())):
    M,N,x,y=map(int,input().split())
    res=-1
    dic={}
    idx=0
    while M*idx+x<=M*N:
        dic[M*idx+x]=1
        idx+=1
    idx=0
    while N*idx+y<=M*N:
        if N*idx+y in dic:
            res=N*idx+y
    print(res)