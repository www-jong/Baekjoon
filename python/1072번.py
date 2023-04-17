import sys
input=sys.stdin.readline
X,Y=map(int,input().split())
Z=(Y*100)//X
res=0
if Z>=99:
    print(-1)
else:
    res=0
    le=1
    ri=X
    while le<=ri:
        mid=(le+ri)//2
        if (Y+mid)*100//(X+mid)<=Z:
            le=mid+1
        else:
            res=mid
            ri=mid-1
    print(res) 