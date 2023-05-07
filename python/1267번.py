import math
N=int(input())
li=list(map(int,input().split()))
Y,M=0,0
for i in li:
    Y+=math.ceil(i/30)*10+(10 if i%30==0 else 0)
    M+=math.ceil(i/60)*15+(15 if i%60==0 else 0)
print("Y "+str(Y) if Y<M else ("Y M "+str(Y) if Y==M else "M "+str(M)))
    