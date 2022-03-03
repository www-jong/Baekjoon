n,k=map(int,input().split())
def e(a):
    m=1
    for i in range(1,a+1):
        m*=i
    return int(m)
print(int(e(n)//(e(k)*e(n-k)))%10007)
