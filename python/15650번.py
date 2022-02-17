n,m=map(int,input().split())
arr=[]

def func():
    if len(arr)==m:
        print(*arr,sep=" ")
        return
    for i in range(1,n+1):
        if i not in arr:
            if len(arr)>=1 and i > arr[-1]:
                arr.append(i)
                func()
                arr.pop()
            elif len(arr)==0:
                arr.append(i)
                func()
                arr.pop()

func()
    
