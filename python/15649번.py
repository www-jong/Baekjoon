n,m=map(int,input().split())

arr=[]

def func():
    if len(arr)==m:
        print(*arr,sep=" ")
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            func()
            arr.pop()
func()
    