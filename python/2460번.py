r=0
x=0
for i in range(10):
    a,b=map(int,input().split())
    r=r+b-a
    x=max(r,x)
print(x)