for n in range(1,4001):
    #n=int(input())
    arr=[]
    a=0
    def func(s,c):
        if s==0:
            arr.append(c)
            return
        for i in range(int(s**(1/2)),0,-1):
            s-=i**2
            c+=1
            func(s,c)
            c-=1
            s+=i**2
    func(n,0)
    print("%d %d"%(n,min(arr)))