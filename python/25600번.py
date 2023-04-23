res=-1
for i in range(int(input())):
    a,d,g=map(int,input().split())
    res=max(res,a*(d+g)*2 if a==(d+g) else a*(d+g))
print(res)