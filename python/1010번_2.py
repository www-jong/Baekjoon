def fac(n):
    num=1
    for i in range(1,n+1):
        num*=i
    return num
# 수학공식,
# mCn --> m! / (m-n)!n!
for _ in range(int(input())):
    n,m=map(int,input().split())
    ans=fac(m)//(fac(n)*fac(m-n))
    print(ans)