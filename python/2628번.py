y,x=map(int,input().split())
li=[[0]*(y+1) for i in range(x+1)]
xcut=[0,x]
ycut=[0,y]
N=int(input())
for i in range(N):
    axis,cutpoint=map(int,input().split())
    if axis==0:
        xcut.append(cutpoint)
    else:
        ycut.append(cutpoint)
xcut.sort()
ycut.sort()
res=-1
for i in range(len(xcut)-1):
    for j in range(len(ycut)-1):
        res=max((xcut[i+1]-xcut[i])*(ycut[j+1]-ycut[j]),res)
print(res)