s=[0]*5
for i in range(int(input())):
    x,y=map(int,input().split())
    if x>0:
        if y>0:
            s[0]+=1
        else:
            s[1]+=1
    elif x<0:
        if y>0:
            s[2]+=1
        else:
            s[3]+=1
    else:
        s[4]+=1
print('Q1: ',s[0])
print('Q2: ',s[2])
print('Q3: ',s[3])
print('Q4: ',s[1])
print('AXIS: ',s[4])
