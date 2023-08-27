N=int(input())
r=0
for i in range(1,N+1):
    if N%i==0:
        r+=i
print(r*5-24)