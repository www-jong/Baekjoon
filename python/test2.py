def moo(k):
    if k==0:
        return "moo"
    
    return moo(k-1)+"m"+"o"*(k+2)+moo(k-1)

moople="_"+moo(15)
for N in range(1,200):
    li=[3]
    check="omoomooomoo"

    ttt=""
    for i in range(1,34):
        li.append(li[i-1]*2+(i+3))

    def func(n,s):
        n-=li[s]
        if n==1:
            return "m"
        if n<=s+4:
            return "o"
        n-=s+4
        if s==0:
            return check[n]
        
        if n>=li[s-1]:
            return func(n,s-1)
        else:
            return func(n+li[s-1]+s+3,s-1)

    if N<=10:
        ttt=check[N]
    else:
        for i in range(1,34):
            if N<li[i]:
                ttt=func(N,i-1)
                break
            elif N==li[i]:
                ttt="o"
                break
    if moople[N]==ttt:
        print(f'{N} : {ttt}')
    else:
        print(f"{N} ___ No -> {ttt} -< {moople[N]}")
print(moo(2))