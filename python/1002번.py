import sys
for i in range(int(sys.stdin.readline())):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    r3=abs(((x2-x1)**2+(y2-y1)**2)**(1/2))
    