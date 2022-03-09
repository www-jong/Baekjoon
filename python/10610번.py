n=input()
N=int(n)
arr=list(n)
check=""
ar=[]
answer=0
if "0" not in arr:
    print("-1")
else:
    def func():
        global check
        global answer
        for i in ar:
            check+=ar[i]
        if check is not None:
         if int(check)%30==0:
             answer=int(check)
             return
        for i in range(0,len(arr)):
            if i in ar:
                continue
            ar.append(i)
            func(ar)
            ar.pop(i)
    func()
if answer ==0:
    print("-1")
else:
    print(answer)    
    