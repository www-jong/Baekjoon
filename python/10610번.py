n=input()
arr=list(n)
ar=[]
answer=0
if "0" not in arr:
    print("-1") 
else:
    def func():
        check=""
        global answer
        if len(ar)==len(arr):
            for i in ar:
                check+=arr[i]
            if int(check)%30==0 and int(check)>answer:
                answer=int(check)
                return
        for i in range(0,len(arr)):
            if i in ar:
                continue
            ar.append(i)
            func()
            ar.pop()
    func()
    if answer ==0:
        print("-1")
    else:
        print(answer)    
    