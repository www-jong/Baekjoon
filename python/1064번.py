x1,y1,x2,y2,x3,y3=map(int,input().split())
def length(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
A=length(x1,x2,y1,y2)
B=length(x1,x3,y1,y3)
C=length(x2,x3,y2,y3)
maxlen=max(A+B,A+C,B+C)
minlen=min(A+B,A+C,B+C)
if x1==x2==x3 or y1==y2==y3:
    print(-1)
elif ((y2-y1)/(x2-x1 if x2-x1!=0 else 1))==((y3-y2)/(x3-x2 if x3-x2!=0 else 1))==((y3-y1)/(x3-x1 if x3-x1!=0 else 1)):
    print(-1)
else:
    print((maxlen-minlen)*2)
