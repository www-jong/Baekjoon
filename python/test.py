N=int(input())
li=[3]
check="omoomooomoo"

for i in range(1,34):
    li.append(li[i-1]*2+(i+3))

def func(n,s):
    if n<=10:
        print(check[n])
        return
    if n==1:
        print("m")
        return
    elif n<=s+4:
        print("o")
        return
    else:
        n-=s+4
        if n>li[s-1]:
            func(n-li[s-1],s-1)
        elif n==li[s-1]:
            print("o")
            return
        else:
            func(n,s-1)
if N<=10:
    print(check[N])
else:
    for i in range(34):
        if N<li[i]:
            func(N-li[i-1],i-1)
            break
        elif N==li[i]:
            print("o")
            break