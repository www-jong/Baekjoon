
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    ans=0
    def func(s):
        global ans
        if len(arr)==n:
             ans+=1
             return
        for i in range(s,m):
            arr.append(i)
            func(s+1)
            arr.pop()
    func(0)
    print(ans)