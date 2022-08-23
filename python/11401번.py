n,k=map(int,input().split())
a,b=1,1
m=1000000007
for i in range(1,n+1):
    if i<=k:
        b*=i
    if i<=(n-k):
        b*=i
    a*=i
    if a>m:a=a%m
    if b>m:b=b%m
def suq(x,y):
    if y==0:
        return 1
    elif y==1:
        return x
    tmp=suq(x,y//2)
    if y%2==0:
        return tmp*tmp%m
    else:
        return tmp*tmp*x%m
print(a*suq(b,m-2)%m)
#print(int(a/b%1000000007))


'''
(n,k) -> n!/(k!(n-k)!)  0<=k<=n
         0     k<0 or k>n
페르마의 소정리 이용
페르마 소정리 : 
    p가 소수, a가 정수일 때
    a^p ≡ a (mod p)  --> p로 나눈 나머지가 같다
    이식의 양변을 a^2로 나누어 주면
    a^(p-2) ≡ 1/a (mod p) 

A=N!, B=(K!(N-K)!) , M=1,000,000,007이라 할 때,
A/B (mod M)  M은 소수 를 구해야 함
M이 소수이므로, A*B^(M-2) (mod M) 을 구해야 함

'''