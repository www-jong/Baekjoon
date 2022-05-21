n=int(input())
sted='*'*n+' '*(2*(n-2)+1)+'*'*n
middle='*'+' '*(n-2)+'*'
for i in range(1,n):
    if i==1:
        print(sted)
    else:
        print(' '*(i-1)+middle+' '*(2*(n-1-i)+1)+middle)
print(' '*(n-1)+'*'+' '*(n-2)+'*'+' '*(n-2)+'*')
for i in range(n-1,0,-1):
    if i==1:
        print(sted)
    else:
        print(' '*(i-1)+middle+' '*(2*(n-1-i)+1)+middle)