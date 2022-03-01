while True:
    m=list(map(int,input().split()))
    a=m[1:m[0]+1]
    if m[0]==0:break
    arr=[]
    def func():
        if len(arr)==6:
            print(*arr,sep=" ")
            return
        for i in a:
            if i not in arr:
                if len(arr)>=1:
                    if arr[-1]>i:continue
                arr.append(i)
                func()
                arr.pop()
    func()
    print()

