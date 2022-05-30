import math
w,h,x,y,p=map(int,input().split())
li=0
for i in range(p):
    mx,my=map(int,input().split())
    if (x-mx)**2+(y+h/2-my)**2<=(h/2)**2 or (x+w-mx)**2+(y+h/2-my)**2<=(h/2)**2 or (x<=mx<=x+w and y<=my<=y+h):
        li+=1
print(li)