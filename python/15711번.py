MAXS=10**6+1
primes=[True]*(MAXS)
for i in range(2,int(MAXS**0.5)+1):
    if primes[i]:
        for j in range(i*i,MAXS,i):
            primes[j]=False


def check(a,b):
    if a+b<=10**6:
        return primes

N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    print(check(a,b))
