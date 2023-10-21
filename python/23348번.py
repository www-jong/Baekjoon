A,B,C=map(int,input().split())
res=0
for i in range(int(input())):
    r=0
    for j in range(3):
        a,b,c=map(int,input().split())
        r+=a*A+b*B+c*C
    res=max(r,res)
print(res)