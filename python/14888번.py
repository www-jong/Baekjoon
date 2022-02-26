n,m=map(int,input().split())

arr=[]


def func():
    maxv=-1e9
    minv=1e9
    def ffun():
        nonlocal maxv
        nonlocal minv
        val=nums[0]
        if len(arr)==n-1:
            for i in range(n-1):
                val+=nums[1]
            return
        for i in sepa:
            arr.append(i)
            func()
            arr.pop()
    ffun()
    return maxv,minv


count=0
arr=[]
nums=list(map(int,input().split()))
sepas=list(map(int,input().split()))
sepa=[1]*sepas[0]+[2]*sepas[1]+[3]*sepas[2]+[4]*sepas[3]
maxv,minv=func()
print(maxv)
print(minv)
    
    

    