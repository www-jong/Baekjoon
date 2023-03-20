T=int(input())
for i in range(T):
    N=int(input())
    li=[0]*(N+1)
    for i in range(2,N+1):
        for j in range(i,N+1):
            if j%i==0:
                li[j]=0 if li[j]==1 else 1
    print(li.count(0)-1)