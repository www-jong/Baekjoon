N=int(input())
check=[0,0]+[1]*(N-1)
primes=[]

for i in range(2,N+1):
    if check[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            check[j]=0

st=0
end=0
sums=0
while primes[end]<N:
    

print(primes)