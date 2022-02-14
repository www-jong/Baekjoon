n=int(input())
arr1=list(map(int,input().split()))
arr2=list(set(arr1))
arr2.sort()
res1=[0 for _ in range(n)]
di={}
for i in range(len(arr2)):
    di[arr2[i]]=i
for i in range(n):
    print(di[arr1[i]],end=' ')
