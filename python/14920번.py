N=int(input())
r=1
while N!=1:
    if N%2==0:
        N//=2
    else:
        N=3*N+1
    r+=1
print(r)