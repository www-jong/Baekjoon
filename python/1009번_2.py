import sys
for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    c=a**(b%4 if b%4!=0 else 4)%10
    print(c if c!=0 else 10)


