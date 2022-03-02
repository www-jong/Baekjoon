L,C=map(int,input().split())
a=list(map(str,input().split()))
check=['a','e','i','o','u']
arr=[]
a.sort()
def func(s,m,j):
    if len(arr)==L:
        if m>=1 and j>=2:
            print(*arr,sep="")
            return
        return
    for i in range(s,len(a)):
        if a[i] in check:
            m+=1
            arr.append(a[i])
            func(i+1,m,j)
            m-=1
        else:
            j+=1
            arr.append(a[i])
            func(i+1,m,j)
            j-=1
        arr.pop()
func(0,0,0)