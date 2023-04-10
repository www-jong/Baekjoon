x,k=map(int,input().split())
li,res=[k*7,k*3.5,k*1.75],0
for i in li:
    if i<=x:
        res=max(res,i*1000)

print(max(int(res),0))