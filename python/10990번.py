n=int(input())
for i in range(n):
    print(' '*(n-1-i)+'*'+' '*(i*2-1)+'*'*(1 if i>0 else 0))