import math
while True:
    s=int(input())
    li=[]
    if s==-1:break
    for i in range(1,math.ceil(s/2)+1):
        if s%i==0:li.append(i)
    if sum(li)==s:
        print("%d = %s"%(s," + ".join(str(i) for i in li)))
        #print(li)
    else:
        print("%d is Not perfect."%(s))