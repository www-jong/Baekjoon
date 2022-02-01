import math

for i in range(int(input())):
    x,y=map(int,input().split())
    l=(y-x)**0.5
    if l%1==0:
        print(2*int(l)-1)
    elif y-x<=math.floor(l)**2+math.floor(l):
        print(2*math.ceil(l)-2)
    else:
        print(2*math.ceil(l)-1)

