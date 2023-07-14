N=int(input())
check=[0,0]+[1]*(N-1)
primes=[]

for i in range(2,N+1):
    if check[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            check[j]=0
if N!=1:
    st=0
    end=0
    sums=primes[st]
    res=0
    while end<len(primes):
        if sums==N:
            res+=1
            sums-=primes[st]
            st+=1
        elif sums<N:
            if end<len(primes)-1:
                end+=1
                sums+=primes[end]
            else:
                break
        else:
            if st==end:
                break
            sums-=primes[st]
            st+=1
        #print(f'now : {st}:{end} --> {sums}')
    #print(primes)
    print(res)
else:
    print(0)