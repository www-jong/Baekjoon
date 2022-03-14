n,k=map(int,input().split())
a=[1 for i in range(n+1)]
count=0
for i in range(2,n+1):
    if a[i]==1:
        for j in range(i,n+1,i):
            if a[j]==1:
                a[j]=0
                count+=1
                if count==k:
                    print(j)
                    break
