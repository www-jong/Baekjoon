N,B=map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))

def func(li1,li2):
    tmp=0
    for i in range(N):
        tmp+=li1[i]*li2[i]
    return tmp%1000

def multi(a,b):
    tmp=[[] for _ in range(N)]
    emp=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i].append(b[j][i])

    for i in range(N):
        for j in range(N):
            tem=func(a[i],tmp[j])
            emp[i][j]=tem
    return emp

def sqrt(a,b):
    if b==1:
        for i in range(N):
            for j in range(N):
                a[i][j]%=1000
        return a
    elif b%2==0:
        tmp=sqrt(a,b//2)
        return multi(tmp,tmp)
    else:
        tmp=sqrt(a,b//2)
        return multi(multi(tmp,tmp),a)
ans=sqrt(A,B)
for i in range(N):
    print(*ans[i])