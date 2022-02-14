n=int(input())
arr=["0" for _ in range(n)]
resarr=[]
count=0
lle=[0 for _ in range(51)]
for i in range(n):
    arr[i]=input()
arr=list(set(arr))
arr.sort(key=len)
for i in range(len(arr)):
    lle[len(arr[i])]+=1
for i in range(1,51):
    resarr+=sorted(arr[count:count+lle[i]])
    count+=lle[i]
for i in range(len(resarr)):
    print(resarr[i])


    