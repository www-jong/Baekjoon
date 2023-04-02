import sys
sys.set_int_max_str_digits(1000000)
res=1
n=int(input())
if n==0:
    print(0)
else:
    for i in range(1,n+1):
        res*=i
    print(res)
'''
N = int(input())

if N == 0 :
    print(1)
else :
    result = 1
    for i in range(2, N+1) :
        result *= i
    print(result)
'''