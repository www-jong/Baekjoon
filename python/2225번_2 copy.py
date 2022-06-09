n,k=map(int,input().split())
arr=[]
count=0
def func():
    global count
    if sum(arr)>=n:return
    if len(arr)==k:
        if sum(arr)==n:
            count+=1
            return
        return
    for i in range(0,n+1):
        arr.append(i)
        func()
        arr.pop()
func()
print(count%1000000000)