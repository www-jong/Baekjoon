from collections import deque
primes=[1]*(1001)
so=set()
A,B=map(int,input().split())
C,D=map(int,input().split())
A_s=set()
B_s=set()
for i in range(2,1001):
    if primes[i]:
        primes[i]=1
        so.add(i)
        if A<=i<=B:
            A_s.add(i)
        if C<=i<=D:
            B_s.add(i)
        for j in range(i*i,1001,i):
            primes[j]=0
dust=set()
tot=A_s&B_s
A_s=A_s-tot
B_s=B_s-tot
tot=deque(sorted(list(tot)))
res=0
a,b=0,0
while True:
    check=0
    if res%2==0:
        if tot:
            while tot:
                i=tot.pop()
                if i not in dust:
                    dust.add(i)
                    check=1
                    break
        else:
            while A_s:
                i=A_s.pop()
                if i not in dust:
                    dust.add(i)
                    check=1
                    break
    else:
        if tot:
            while tot:
                i=tot.popleft()
                if i not in dust:
                    dust.add(i)
                    check=1
                    break
        else:
            while B_s:
                i=B_s.pop()
                if i not in dust:
                    dust.add(i)
                    check=1
                    break

    if not check:
        print("yt" if res%2 else "yj")
        break
    res+=1