import sys
input=sys.stdin.readline
k,l=input().split()
c=0
for i in range(2,int(l)):
    if int(k)%i==0:
        print("BAD",i)
        c=1
        break
if not c:
    print("GOOD")