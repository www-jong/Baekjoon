
a=1
for i in range(3):
    a*=int(input())
arr=list(map(int,str(a)))
b=[0,0,0,0,0,0,0,0,0,0]
for i in arr:
    b[i]+=1
for i in range(10):
    print(b[i])



