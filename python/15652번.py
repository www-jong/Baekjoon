n,m=map(int,input().split())
arr=[]
def func():
    if len(arr)==m:
        print(*arr,sep=" ")
        return
    elif len(arr)==0 or m==1:
        for i in range(1,n+1):
            arr.append(i)
            func()
            arr.pop()
    else:
        for i in range(arr[-1],n+1):
            arr.append(i)
            func()
            arr.pop()
func()