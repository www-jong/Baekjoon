k,w,m=map(int,input().split())
res=(w-k)//m
print(res+(1 if (w-k)%m!=0 else 0))