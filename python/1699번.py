n=int(input())
a=0
while n!=0:
    n-=int(n**(1/2))**2
    a+=1
print(a)        