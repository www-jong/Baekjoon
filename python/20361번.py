N,X,K=map(int,input().split())
res=X
for i in range(K):
    a,b=map(int,input().split())
    if a==res:
        res=b
    elif b==res:
        res=a
print(res)