a,b=map(int,input().split())
c,d=map(int,input().split())
A,B=(b*c)+(a*d),b*d
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
C=gcd(A,B)
print(f"{A//C} {B//C}")