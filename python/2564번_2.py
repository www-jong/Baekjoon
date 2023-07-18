import sys
input=sys.stdin.readline

def dis(loc,dist):
    if loc==1:
        return dist
    elif loc==4:
        return w+dist
    elif loc==2:
        return 2*w+h-dist
    elif loc==3:
        return 2*(w+h)-dist

w,h=map(int,input().split())
N=int(input())
loc=[0]*(N+1)
dists=[]
for i in range(N+1):
    loc,dist=map(int,input().split())
    dists.append(dis(loc,dist))

d_dist=dists[-1]
res=0
for i in range(N):
    tmp=abs(dists[i]-d_dist)
    tot=2*(w+h)
    res+=min(tmp,tot-tmp)
print(res)