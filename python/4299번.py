A,B=map(int,input().split())
if A+B<0 or A-B<0 or (A+B)%2:
    print(-1)
else:
    a,b=(A+B)//2,A-(A+B)//2
    print(max(a,b),min(a,b))