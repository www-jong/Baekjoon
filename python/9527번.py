import math,sys
sys.setrecursionlimit(10**9)
A,B=map(int,input().split())
res=0
pnum=[0]*(100)
for i in range(1,100):
    pnum[i]=2**(i-1)+2*(pnum[i-1])

def check(n):
    if n<=0:
        return 0

    x=int(math.log2(n)) #   2**x<=n<=2**(x+1)
    if 2**x==n:
        return x*n//2+1
    
    diff=n-2**x
    return check(2**x)+diff+check(diff)
print(check(B)-check(A-1))
'''
000 ->0
001 ->1
010 ->2
011 ->3
100 ->4
101 ->5
110 ->6
111 ->7

1000 ->8
1001 ->9
1010 ->10
1011 ->11
1100 ->12
1101 ->13
1110 ->14
1111 ->15

2**n -1 인수의 1의 갯수는 2**n /2 개임.
이때, 만약 애매한 숫자인 13 같은 경우
규칙성이 존재.
첫 1을 제외하고, 8에서 13까지는  0에서 5까지의 진수랑 같음!

2**n <= 13 <= 2**(n+1) 을 만족하는 n을 구함(여기선 3)
우선 2**3 -1인 수의 1의 갯수를 구하고,  
gap인 13- 2**3  을 구함. = 5
앞자리의 1의 갯수 1*5 와 5의 1갯수를 세주면 끝.
이를 재귀로 처리

'''