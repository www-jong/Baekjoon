x=int(input())
n=int(input())
m=0
for i in range(n):
    a,b=map(int,input().split())
    m+=a*b
if m!=x:
    print("No")
else:
    print("Yes")