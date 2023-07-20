def moo(k):
    if k==0:
        return "moo"
    
    return moo(k-1)+"m"+"o"*(k+2)+moo(k-1)

moople="_"+moo(15)
for N in range(1,100):
    li=[3]
    check="omoomooomoo"

    ttt=""
    for i in range(1,34):
        li.append(li[i-1]*2+(i+3))

    def func(n,s):
        if n<=10 and s==0:
            return check[n]
        if n==1:
            return "m"
        elif n<=s+4:
            return "o"
        else:
            n-=s+4
            if n>li[s-1]:
                return func(n-li[s-1],s-1)
            elif n==li[s-1]:
                return "o"
            else:
                return func(n,s-2)
    if N<=10:
        ttt=check[N]
    else:
        for i in range(34):
            if N<li[i]:
                ttt=func(N-li[i-1],i-1)
                break
            elif N==li[i]:
                ttt="o"
                break
    if moople[N]==ttt:
        print(f'{N} : {ttt}')
    else:
        print(f"{N} ___ No")
print(moo(2))