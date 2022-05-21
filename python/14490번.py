import math
a,b=map(int,input().split(':'))
c=math.gcd(a,b)
print('%d:%d'%(a/c,b/c))