N=int(input())
li=[3]
check="omoomooomoo"

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
    print(check[N])
else:
    for i in range(34):
        if N<li[i]:
            print(func(N,i-1))
            break
        elif N==li[i]:
            print("o")
            break